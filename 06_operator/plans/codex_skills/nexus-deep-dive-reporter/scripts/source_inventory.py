#!/usr/bin/env python
"""Read-only source inventory helper for NEXUS deep-dive reports.

The script searches supported text-like files and indexes unsupported binaries
as extraction gaps. It writes nothing and prints JSON to stdout.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import zipfile
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree


DEFAULT_ROOTS = [
    r"C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\07_reference_material",
    r"C:\Users\mason\Documents\PROJECTS\PRE_DRAFT_BASE_V1",
    r"C:\Users\mason\Documents\PROJECTS\NEXUS_PIECES_CLAUDE_DATA_DIGESTION",
    r"C:\Users\mason\Documents\PROJECTS\MISC_INFO\NEXUS_REFRENCE",
    r"C:\Users\mason\Documents\PROJECTS\older sub systems built",
    r"C:\Users\mason\.codex\session_index.jsonl",
    r"C:\Users\mason\.codex\sessions",
]

DEFAULT_TERMS = [
    "KAIROS",
    "KAIROZ",
    "KAIROZ 111",
    "KAIROS 1.0",
    "KAIROZ 1.0",
    "OPTIMUS PRIME",
    "AKARA",
    "AEGIS",
    "AEGIS OS",
    "AEGIS_OS",
    "NEXUS",
    "NEXUS_SUXEN",
    "SUXEN",
    "SOVEREIGN COUNCIL",
    "SOVERIGN COUNCIL",
    "SOVEREIGNTY COUNCIL",
    "JOYBOY",
    "MYTHOS PRIME AXIOM",
    "PRIME AXIOM",
    "HEKATE",
    "WAVE-3",
    "VAELION",
]

TEXT_EXTENSIONS = {".md", ".txt", ".json", ".csv", ".log"}
DOCX_EXTENSIONS = {".docx"}
GAP_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".bmp",
    ".tif",
    ".tiff",
    ".zip",
    ".7z",
    ".rar",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".sqlite",
    ".db",
    ".pyc",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inventory NEXUS deep-dive sources.")
    parser.add_argument("--root", action="append", default=[], help="File or directory root to scan. Repeatable.")
    parser.add_argument("--nexus-defaults", action="store_true", help="Scan the default NEXUS deep-dive roots.")
    parser.add_argument("--query", action="append", default=[], help="Search term. Repeatable.")
    parser.add_argument("--terms-file", help="Text/markdown file containing one term per line.")
    parser.add_argument("--max-file-bytes", type=int, default=2_000_000, help="Skip text extraction above this size.")
    parser.add_argument("--max-matches-per-file", type=int, default=10, help="Limit snippets per matched file.")
    parser.add_argument("--context-chars", type=int, default=160, help="Characters of context on each side of a hit.")
    return parser.parse_args()


def load_terms(args: argparse.Namespace) -> list[str]:
    terms: list[str] = []
    terms.extend(args.query)
    if args.terms_file:
        terms.extend(read_terms_file(Path(args.terms_file)))
    if not terms:
        terms.extend(DEFAULT_TERMS)
    return dedupe([clean_term(term) for term in terms if clean_term(term)])


def read_terms_file(path: Path) -> list[str]:
    if not path.exists():
        return []
    raw = read_text(path, max_file_bytes=1_000_000)
    terms: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        stripped = stripped.lstrip("-*").strip()
        stripped = stripped.strip("`").strip()
        if stripped and not stripped.startswith("|"):
            terms.append(stripped)
    return terms


def clean_term(term: str) -> str:
    return term.strip().strip("\"'").strip()


def dedupe(items: Iterable[str]) -> list[str]:
    seen = set()
    ordered = []
    for item in items:
        key = item.casefold()
        if key not in seen:
            ordered.append(item)
            seen.add(key)
    return ordered


def roots_from_args(args: argparse.Namespace) -> list[Path]:
    roots = [Path(root) for root in args.root]
    if args.nexus_defaults:
        roots.extend(Path(root) for root in DEFAULT_ROOTS)
    if not roots:
        roots.append(Path.cwd())
    return roots


def iter_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        yield root
        return
    if not root.exists():
        return
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in {".git", "node_modules", ".venv", "__pycache__"}]
        for filename in filenames:
            yield Path(dirpath) / filename


def classify_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in TEXT_EXTENSIONS:
        return "searchable-text"
    if suffix in DOCX_EXTENSIONS:
        return "searchable-docx"
    if suffix in GAP_EXTENSIONS:
        return "extraction-gap"
    return "unsupported"


def read_text(path: Path, max_file_bytes: int) -> str:
    if path.stat().st_size > max_file_bytes:
        raise ValueError("file exceeds max-file-bytes")
    for encoding in ("utf-8-sig", "utf-8", "utf-16", "cp1252"):
        try:
            return path.read_text(encoding=encoding, errors="replace")
        except UnicodeError:
            continue
    return path.read_text(errors="replace")


def read_docx_text(path: Path, max_file_bytes: int) -> str:
    if path.stat().st_size > max_file_bytes:
        raise ValueError("file exceeds max-file-bytes")
    chunks: list[str] = []
    with zipfile.ZipFile(path) as archive:
        names = [
            name
            for name in archive.namelist()
            if name.startswith("word/")
            and name.endswith(".xml")
            and any(part in name for part in ("document", "header", "footer", "footnotes", "endnotes"))
        ]
        for name in names:
            xml_bytes = archive.read(name)
            try:
                root = ElementTree.fromstring(xml_bytes)
            except ElementTree.ParseError:
                continue
            for element in root.iter():
                if element.text:
                    chunks.append(element.text)
    return " ".join(chunks)


def make_patterns(terms: list[str]) -> list[tuple[str, re.Pattern[str]]]:
    patterns = []
    for term in terms:
        patterns.append((term, re.compile(re.escape(term), re.IGNORECASE)))
    return patterns


def snippet(text: str, start: int, end: int, context_chars: int) -> str:
    left = max(0, start - context_chars)
    right = min(len(text), end + context_chars)
    raw = text[left:right].replace("\r", " ").replace("\n", " ")
    return re.sub(r"\s+", " ", raw).strip()


def search_text(text: str, patterns: list[tuple[str, re.Pattern[str]]], max_matches: int, context_chars: int) -> list[dict[str, object]]:
    matches: list[dict[str, object]] = []
    for term, pattern in patterns:
        for hit in pattern.finditer(text):
            matches.append(
                {
                    "term": term,
                    "start": hit.start(),
                    "end": hit.end(),
                    "snippet": snippet(text, hit.start(), hit.end(), context_chars),
                }
            )
            if len(matches) >= max_matches:
                return matches
    return matches


def inventory_file(path: Path, patterns: list[tuple[str, re.Pattern[str]]], args: argparse.Namespace) -> dict[str, object]:
    file_class = classify_file(path)
    record: dict[str, object] = {
        "path": str(path),
        "class": file_class,
        "size_bytes": safe_size(path),
        "matches": [],
        "gap_reason": None,
        "error": None,
    }
    try:
        if file_class == "searchable-text":
            text = read_text(path, args.max_file_bytes)
            record["matches"] = search_text(text, patterns, args.max_matches_per_file, args.context_chars)
        elif file_class == "searchable-docx":
            text = read_docx_text(path, args.max_file_bytes)
            record["matches"] = search_text(text, patterns, args.max_matches_per_file, args.context_chars)
        elif file_class == "extraction-gap":
            record["gap_reason"] = "requires second-pass extraction or OCR"
        else:
            record["gap_reason"] = "unsupported extension"
    except Exception as exc:  # noqa: BLE001 - report inventory errors without stopping the run.
        record["error"] = f"{type(exc).__name__}: {exc}"
    return record


def safe_size(path: Path) -> int | None:
    try:
        return path.stat().st_size
    except OSError:
        return None


def main() -> int:
    args = parse_args()
    terms = load_terms(args)
    patterns = make_patterns(terms)
    roots = roots_from_args(args)

    files_seen = 0
    matched_files = []
    extraction_gaps = []
    unreadable_or_errors = []
    missing_roots = []

    for root in roots:
        if not root.exists():
            missing_roots.append(str(root))
            continue
        for path in iter_files(root):
            files_seen += 1
            record = inventory_file(path, patterns, args)
            if record.get("matches"):
                matched_files.append(record)
            elif record.get("class") == "extraction-gap":
                extraction_gaps.append(record)
            elif record.get("error"):
                unreadable_or_errors.append(record)

    output = {
        "status": "observational",
        "mutated_files": False,
        "terms": terms,
        "roots": [str(root) for root in roots],
        "missing_roots": missing_roots,
        "files_seen": files_seen,
        "matched_file_count": len(matched_files),
        "extraction_gap_count": len(extraction_gaps),
        "error_count": len(unreadable_or_errors),
        "matched_files": matched_files,
        "extraction_gaps": extraction_gaps,
        "unreadable_or_errors": unreadable_or_errors,
    }

    json.dump(output, sys.stdout, indent=2, ensure_ascii=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

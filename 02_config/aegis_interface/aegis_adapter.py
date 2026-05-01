
def format_aegis_advisory(domain, suggestion):
    return {
        "type": "AEGIS_ADVISORY",
        "domain": domain,
        "suggestion": suggestion,
        "authority": "NON_EXECUTABLE"
    }

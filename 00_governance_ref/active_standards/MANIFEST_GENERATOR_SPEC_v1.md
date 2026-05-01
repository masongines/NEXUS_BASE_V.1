# MANIFEST_GENERATOR_SPEC_v1

Classification: Active Standard  
Authority: Non-Doctrinal  
Layer: Governance Kernel  

Purpose:
Automatically generate KERNEL_MANIFEST.json from local files.

Rules:
- Doctrine identity comes ONLY from DOCTRINE_IDENTITY_REGISTRY.md
- Manifest is observational only
- No manual counts allowed

Core Logic:
1. Scan governance_kernel folder
2. Parse doctrine registry
3. Classify files
4. Generate counts
5. Output manifest

Safeguards:
- No modification of source files
- No doctrine promotion
- Fail if registry mismatch

End State:
Reliable inventory with zero manual overhead.
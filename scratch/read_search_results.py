import os

file_path = r"c:\Users\mks1j\.gemini\antigravity\scratch\search_results.txt"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

print("Lines containing 404 or Not found or not indexed:")
print("="*60)
for i, line in enumerate(lines):
    if any(term in line.lower() for term in ["404", "not found", "not-found", "error"]):
        print(f"Line {i+1}: {line.strip()[:150]}")
print("="*60)

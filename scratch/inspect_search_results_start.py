import os

file_path = r"c:\Users\mks1j\.gemini\antigravity\scratch\search_results.txt"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    for i in range(20):
        line = f.readline()
        if not line:
            break
        print(f"Line {i+1}: {line.strip().encode('ascii', errors='backslashreplace').decode('ascii')}")

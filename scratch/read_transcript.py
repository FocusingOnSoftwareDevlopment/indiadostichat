import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

transcript_path = r"C:\Users\mks1j\.gemini\antigravity\brain\c537d5f0-7d36-425b-9fa7-d2e897850b4e\.system_generated\logs\transcript.jsonl"

try:
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line)
            if data.get("type") == "USER_INPUT":
                print(f"Step {data.get('step_index')}: {data.get('content')}")
except Exception as e:
    print(f"Error: {e}")

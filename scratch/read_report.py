import json

with open("report.json", "r", encoding="utf-8") as f:
    data = json.load(f)

audits = data.get("audits", {})

reflow = audits.get("forced-reflow", {})
print("Forced reflow score:", reflow.get("score"))
print("Forced reflow displayValue:", reflow.get("displayValue"))
print("Forced reflow explanation:", reflow.get("explanation"))
print("Forced reflow details:", reflow.get("details"))

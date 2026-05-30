import json
import os

report_path = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\report.json"

if not os.path.exists(report_path):
    print("ERROR: report.json not found")
    exit(1)

with open(report_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

audits = data.get('audits', {})
network_requests = audits.get('network-requests', {}).get('details', {}).get('items', [])

print("Image requests captured during Lighthouse audit:")
print("="*60)
for item in network_requests:
    url = item.get('url', '')
    if any(ext in url.lower() for ext in ['.png', '.jpg', '.webp', '.svg', '.gif']):
        transfer_kb = item.get('transferSize', 0) / 1024
        print(f"- {url} ({transfer_kb:.2f} KB)")
print("="*60)

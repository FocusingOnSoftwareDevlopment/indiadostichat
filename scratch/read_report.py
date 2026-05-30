import json
import os

report_path = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\report.json"

if not os.path.exists(report_path):
    print("ERROR: report.json not found")
    exit(1)

with open(report_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract scores
categories = data.get('categories', {})
perf_score = categories.get('performance', {}).get('score', 0) * 100
acc_score = categories.get('accessibility', {}).get('score', 0) * 100
bp_score = categories.get('best-practices', {}).get('score', 0) * 100
seo_score = categories.get('seo', {}).get('score', 0) * 100

# Extract audits
audits = data.get('audits', {})
fcp = audits.get('first-contentful-paint', {}).get('displayValue', 'N/A')
lcp = audits.get('largest-contentful-paint', {}).get('displayValue', 'N/A')
si = audits.get('speed-index', {}).get('displayValue', 'N/A')
tbt = audits.get('total-blocking-time', {}).get('displayValue', 'N/A')
cls = audits.get('cumulative-layout-shift', {}).get('displayValue', 'N/A')

# Calculate transfer size
network_requests = audits.get('network-requests', {}).get('details', {}).get('items', [])
total_bytes = sum(item.get('transferSize', 0) for item in network_requests)
total_kb = total_bytes / 1024

print("\n" + "="*40)
print("Local Lighthouse Mobile Results:")
print("="*40)
print(f"Performance Score:   {perf_score:.0f}")
print(f"Accessibility Score: {acc_score:.0f}")
print(f"Best Practices:      {bp_score:.0f}")
print(f"SEO:                 {seo_score:.0f}")
print("-"*40)
print(f"FCP:                 {fcp}")
print(f"LCP:                 {lcp}")
print(f"Speed Index:         {si}")
print(f"TBT:                 {tbt}")
print(f"CLS:                 {cls}")
print(f"Total Transfer Size: {total_kb:.2f} KB")
print("="*40)

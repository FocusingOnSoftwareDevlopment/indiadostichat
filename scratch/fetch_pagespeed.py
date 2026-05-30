import urllib.request
import json
import time

url = "https://www.indiadostichat.com/"
api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile"

print("Waiting 30 seconds for GitHub Pages deployment to complete...")
time.sleep(30)

print(f"Requesting PageSpeed Insights for strategy=mobile on {url}...")
try:
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
    # Get categories
    categories = data.get('lighthouseResult', {}).get('categories', {})
    perf_score = categories.get('performance', {}).get('score', 0) * 100
    acc_score = categories.get('accessibility', {}).get('score', 0) * 100
    bp_score = categories.get('best-practices', {}).get('score', 0) * 100
    seo_score = categories.get('seo', {}).get('score', 0) * 100
    
    # Get metrics
    audits = data.get('lighthouseResult', {}).get('audits', {})
    fcp = audits.get('first-contentful-paint', {}).get('displayValue', 'N/A')
    lcp = audits.get('largest-contentful-paint', {}).get('displayValue', 'N/A')
    si = audits.get('speed-index', {}).get('displayValue', 'N/A')
    tbt = audits.get('total-blocking-time', {}).get('displayValue', 'N/A')
    cls = audits.get('cumulative-layout-shift', {}).get('displayValue', 'N/A')
    
    # Page size and transfer size
    network_requests = audits.get('network-requests', {}).get('details', {}).get('items', [])
    total_bytes = sum(item.get('transferSize', 0) for item in network_requests)
    total_kb = total_bytes / 1024
    
    print("\n" + "="*40)
    print("PageSpeed Mobile Results:")
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
    
except Exception as e:
    print(f"Error querying PageSpeed: {e}")

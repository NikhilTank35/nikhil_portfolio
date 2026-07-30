import urllib.request
import re

url = "https://www.freelancer.in/u/nikhiltank35"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # Try to find portfolio images. Freelancer usually stores them in a data attribute or img src
    # E.g., https://cdn2.f-cdn.com/files/download/....
    urls = set()
    for match in re.finditer(r'https://cdn[0-9]\.f-cdn\.com/files/download/[^"\s\']+', html):
        urls.add(match.group(0))
    for match in re.finditer(r'https://cdn[0-9]\.f-cdn\.com/ppic/[^"\s\']+', html):
        if 'portfolio' in match.group(0).lower() or 'projects' in match.group(0).lower() or '.jpg' in match.group(0) or '.png' in match.group(0):
            urls.add(match.group(0))
            
    print("Found URLs:", len(urls))
    for u in urls:
        print(u)
        
except Exception as e:
    print("Error:", e)

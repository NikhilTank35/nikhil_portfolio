import re

with open('freelancer.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
    
# Find all URLs looking like images
urls = set()
for match in re.finditer(r'https?://[^"\s\'\\]+', content):
    url = match.group(0)
    if 'portfolio' in url.lower() or 'project' in url.lower() or '.jpg' in url or '.png' in url or 'image' in url:
        urls.add(url)

for u in urls:
    if 'cdn' in u or 'f-cdn' in u:
        print(u)

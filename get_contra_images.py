import urllib.request
import re
import json

url = "https://contra.com/nikhil_tank_ujts4680/work?r=nikhil_tank_ujts4680"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Contra uses Next.js, let's look for __NEXT_DATA__
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>', html)
    if match:
        data = json.loads(match.group(1))
        print("Found NEXT_DATA")
        # dump part of data to file or extract images
        # We want to extract project images
        images = set()
        def find_images(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k in ['url', 'src', 'imageUrl', 'coverImage'] and isinstance(v, str) and (v.startswith('http') and ('.png' in v or '.jpg' in v or 'image' in v)):
                        images.add(v)
                    find_images(v)
            elif isinstance(obj, list):
                for item in obj:
                    find_images(item)
        find_images(data)
        for img in images:
            if 'contra.com' in img or 'cloudfront' in img or 'image' in img:
                print("IMG:", img)
    else:
        # Fallback to regex for img tags
        for img in re.findall(r'<img[^>]+src="([^">]+)"', html):
            print("IMG_TAG:", img)
except Exception as e:
    print("Error:", e)

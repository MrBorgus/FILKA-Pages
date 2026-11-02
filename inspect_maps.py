import os
import glob
import re

for folder in ['Riihimaki/en', 'Forssa/en']:
    print(f"=== FOLDER: {folder} ===")
    for path in sorted(glob.glob(f'{folder}/*.html')):
        name = os.path.basename(path)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        
        # Look for text inside body or script or html comments or div tags
        divs = re.findall(r'<div[^>]*>(.*?)</div>', text, re.DOTALL | re.I)
        div_texts = []
        for d in divs:
            cleaned = re.sub(r'<[^>]+>', ' ', d)
            cleaned = ' '.join(cleaned.split())
            if len(cleaned) > 20 and len(cleaned) < 300:
                div_texts.append(cleaned)
        
        print(f"\n--- {name} ---")
        for dt in div_texts[:5]:
            print("  *", dt)


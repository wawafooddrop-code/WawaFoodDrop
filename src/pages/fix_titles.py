import os
import re

pages_dir = '.'
fixed = 0

for fname in os.listdir(pages_dir):
    if not fname.endswith('.html'):
        continue
    
    filepath = os.path.join(pages_dir, fname)
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Find title tags that are missing closing </title> before <link rel="icon">
    # Pattern: <title>...text (no </title>) \n <link rel="icon"
    pattern = r'(<title>[^\n]*?)(\n<link rel="icon"[^\n]*>)'
    replacement = r'\1</title>\2'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed: {fname}')
        fixed += 1
    else:
        print(f'OK: {fname}')

print(f'\nTotal fixed: {fixed}')

import re

files = {
    'customer-orders.html': [(r'https://via\.placeholder\.com/64x64\?text=Food', 'assets/logo.png')],
    'customer-saved.html': [(r'placeholderUrl\(name, 400, 300\)', "'assets/logo.png'")],
    'restaurant-menu.html': [(r'https://lh3\.googleusercontent\.com/aida-public/AB6AXu[^\'"\>\s]*', 'assets/logo.png')],
    'restaurant.html': [(r'https://lh3\.googleusercontent\.com/aida-public/AB6AXu[^\'"\>\s]*', 'assets/logo.png')]
}

for fname, replacements in files.items():
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements:
            content = re.sub(old, new, content)
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {fname}')
    except Exception as e:
        print(f'Error in {fname}: {e}')

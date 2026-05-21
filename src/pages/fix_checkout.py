with open('checkout.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Search for the pattern
for i, line in enumerate(content.split('\n')):
    if 'item.image' in line and 'img alt' in line:
        print(f'Line {i+1}: {repr(line)}')
        # Replace this specific line
        old_line = line
        new_line = line.replace("' + item.image + '", "' + (item.image || 'assets/logo.png') + '")
        if old_line != new_line:
            content = content.replace(old_line, new_line)
            print('Fixed!')

with open('checkout.html', 'w', encoding='utf-8') as f:
    f.write(content)

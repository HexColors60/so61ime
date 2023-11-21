import sys
import os
import re

def change_links(html_file, base_filename):
    with open(html_file, 'r') as f:
        content = f.read()

    # Modify JavaScript links
    pattern = r'<a\s+href="https://web.archive.org/[^"]*javaScript:([^"]+)"'
    content = re.sub(pattern, r'<a href="javaScript:\1"', content)

    new_filename = f"{base_filename}.new.htm"
    with open(new_filename, 'w') as new_file:
        new_file.write(content)

    # Rename the old file
    os.rename(html_file, f"{base_filename}.old.htm")

    # Rename the new file to the original filename
    os.rename(new_filename, html_file)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python change_links.py <html_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    base_filename, _ = os.path.splitext(html_file)
    change_links(html_file, base_filename)

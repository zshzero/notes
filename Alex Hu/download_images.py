"""Download all images from markdown files and rewrite URLs to local paths.

Works for any course directory. Pass the course directory as argument.

Usage:
    python download_images.py "System Design by Alex Hu"
"""
import hashlib
import os
import re
import sys
import time
import requests
from urllib.parse import urlparse, unquote

if len(sys.argv) < 2:
    print("Usage: python download_images.py <course_directory>")
    print('  e.g. python download_images.py "System Design by Alex Hu"')
    exit(1)

COURSE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])
IMAGES_DIR = os.path.join(COURSE_DIR, "images")

if not os.path.isdir(COURSE_DIR):
    print(f"ERROR: Directory not found: {COURSE_DIR}")
    exit(1)

os.makedirs(IMAGES_DIR, exist_ok=True)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

# Pattern to match markdown image syntax: ![alt](url)
# Allow brackets inside alt text (e.g. array notation like [0, 1, 2])
IMG_PATTERN = re.compile(r'(!\[(?:[^\[\]]|\[[^\]]*\])*\])\(([^)]+)\)')

def url_to_local_filename(url):
    """Generate a stable local filename from a URL."""
    parsed = urlparse(url)
    path = unquote(parsed.path)
    # Get the original filename
    basename = os.path.basename(path)
    # If no extension or weird name, use hash
    _, ext = os.path.splitext(basename)
    if not ext or ext.lower() not in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.avif', '.bmp', '.ico'):
        ext = '.png'  # default
    # Use a short hash of the full URL to avoid collisions + original name for readability
    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    # Clean the basename for filesystem safety
    clean_name = re.sub(r'[^\w\-.]', '_', basename)
    if len(clean_name) > 80:
        clean_name = clean_name[:80]
    # Ensure it has the right extension
    if not clean_name.lower().endswith(ext.lower()):
        clean_name = clean_name + ext
    return f"{url_hash}_{clean_name}"


def download_image(url, local_path):
    """Download an image from URL to local path. Returns True on success."""
    if os.path.exists(local_path):
        return True
    try:
        resp = session.get(url, timeout=30, allow_redirects=True)
        if resp.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(resp.content)
            return True
        else:
            print(f"  HTTP {resp.status_code}: {url}")
            return False
    except Exception as e:
        print(f"  Error: {e}: {url}")
        return False


# Scan all .md files in the course directory
md_files = sorted([f for f in os.listdir(COURSE_DIR) if f.endswith('.md')])

if not md_files:
    print(f"No .md files found in {COURSE_DIR}")
    exit(0)

print(f"Found {len(md_files)} markdown files in {COURSE_DIR}")

# First pass: collect all unique image URLs
all_urls = set()
for md_file in md_files:
    md_path = os.path.join(COURSE_DIR, md_file)
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    for match in IMG_PATTERN.finditer(content):
        url = match.group(2)
        if url.startswith("http://") or url.startswith("https://"):
            all_urls.add(url)

print(f"Found {len(all_urls)} unique image URLs to download\n")

# Download all images
url_to_local = {}
downloaded = 0
failed = 0

for i, url in enumerate(sorted(all_urls), 1):
    local_name = url_to_local_filename(url)
    local_path = os.path.join(IMAGES_DIR, local_name)
    relative_path = f"./images/{local_name}"

    print(f"[{i}/{len(all_urls)}] {local_name}...", end=" ")
    if download_image(url, local_path):
        url_to_local[url] = relative_path
        downloaded += 1
        print("OK" if not os.path.exists(local_path) or True else "CACHED")
    else:
        failed += 1
        print("FAILED")

    time.sleep(0.1)

print(f"\nDownloaded {downloaded}/{len(all_urls)} images ({failed} failed)")

# Second pass: rewrite MD files with local paths
print("\nRewriting markdown files...")
for md_file in md_files:
    md_path = os.path.join(COURSE_DIR, md_file)
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    for url, local_path in url_to_local.items():
        content = content.replace(f"]({url})", f"]({local_path})")

    if content != original:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(content)
        count = original.count("](" ) - content.count("](http")
        print(f"  Updated {md_file}")
    else:
        print(f"  No changes: {md_file}")

print("\nDone!")

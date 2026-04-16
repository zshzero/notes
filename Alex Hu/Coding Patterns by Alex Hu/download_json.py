"""Download all raw JSON data from ByteByteGo Coding Patterns course.

This course has multi-level slugs (e.g. two-pointers/introduction-to-two-pointers)
unlike other courses which use single-level slugs.

Usage:
    set BBG_TOKEN=your_jwt_token_here
    python download_json.py
"""
import json
import os
import re
import time
import requests

BASE_URL = "https://bytebytego.com"
COURSE = "coding-patterns"
FIRST_SLUG_PARTS = ["two-pointers", "introduction-to-two-pointers"]
FIRST_SLUG_PATH = "/".join(FIRST_SLUG_PARTS)
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw_json")
TOKEN = os.environ.get("BBG_TOKEN", "")

if not TOKEN:
    print("ERROR: Set BBG_TOKEN environment variable with your JWT token.")
    print("  set BBG_TOKEN=your_token_here")
    exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})
cookies = {"token": TOKEN}

# Step 1: Auto-detect BUILD_ID from the site
print("Detecting BUILD_ID...")
resp = session.get(f"{BASE_URL}/courses/{COURSE}/{FIRST_SLUG_PATH}", cookies=cookies)
if resp.status_code != 200:
    print(f"ERROR: Could not fetch page (HTTP {resp.status_code})")
    exit(1)

match = re.search(r'"buildId"\s*:\s*"([^"]+)"', resp.text)
if not match:
    print("ERROR: Could not find BUILD_ID in page source.")
    exit(1)

BUILD_ID = match.group(1)
print(f"BUILD_ID: {BUILD_ID}")

# Step 2: Fetch first chapter to get TOC with all slugs
print(f"\nFetching TOC from first chapter...")
url = f"{BASE_URL}/_next/data/{BUILD_ID}/courses/{COURSE}/{FIRST_SLUG_PATH}.json"
resp = session.get(url, cookies=cookies, allow_redirects=False)

if resp.status_code != 200:
    print(f"ERROR: Could not fetch first chapter (HTTP {resp.status_code})")
    exit(1)

data = resp.json()
toc = data.get("pageProps", {}).get("toc", [])
if not toc:
    print("ERROR: No TOC found in response.")
    exit(1)

# Extract slugs from TOC — slug is an array of path parts
chapters = []
for entry in toc:
    slug_parts = entry.get("slug", [])
    if slug_parts:
        slug_path = "/".join(slug_parts)
        slug_filename = "-".join(slug_parts)  # for filesystem
    elif entry.get("id"):
        slug_path = entry["id"]
        slug_filename = entry["id"]
    else:
        continue
    chapters.append({
        "slug_path": slug_path,
        "slug_filename": slug_filename,
        "title": entry.get("title", slug_path),
        "chapter": entry.get("chapter", 0),
    })

print(f"Found {len(chapters)} chapters:")
for i, ch in enumerate(chapters):
    print(f"  {i+1:02d}. {ch['title']}")

# Save the first chapter (already have data)
first_filename = f"01-{chapters[0]['slug_filename']}.json" if chapters else f"01-{'-'.join(FIRST_SLUG_PARTS)}.json"
first_json_path = os.path.join(OUTPUT_DIR, first_filename)
if not os.path.exists(first_json_path) and data.get("pageProps", {}).get("code"):
    with open(first_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\n[01/{len(chapters)}] Saved {chapters[0]['slug_filename']}")

# Step 3: Download all chapters
print(f"\nDownloading all chapters...")
failed = []
for idx, ch in enumerate(chapters, 1):
    num = f"{idx:02d}"
    json_path = os.path.join(OUTPUT_DIR, f"{num}-{ch['slug_filename']}.json")

    if os.path.exists(json_path):
        print(f"[{num}/{len(chapters)}] Already have {ch['slug_filename']}")
        continue

    print(f"[{num}/{len(chapters)}] Downloading {ch['slug_filename']}...")
    url = f"{BASE_URL}/_next/data/{BUILD_ID}/courses/{COURSE}/{ch['slug_path']}.json"
    resp = session.get(url, cookies=cookies, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        if data.get("pageProps", {}).get("code"):
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print(f"  OK ({len(data['pageProps']['code'])} bytes)")
        else:
            print(f"  FAILED: no content (may need auth)")
            failed.append(ch['slug_filename'])
    else:
        print(f"  FAILED: HTTP {resp.status_code}")
        failed.append(ch['slug_filename'])

    time.sleep(0.3)

print(f"\nDone! Downloaded {len(chapters) - len(failed)}/{len(chapters)} pages")
if failed:
    print(f"Failed: {', '.join(failed)}")

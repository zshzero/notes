"""Download all raw JSON data from ByteByteGo Tech Resume course.

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
COURSE = "tech-resume"
FIRST_SLUG = "p0-c1-acknowledgements"
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
resp = session.get(f"{BASE_URL}/courses/{COURSE}/{FIRST_SLUG}", cookies=cookies)
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
url = f"{BASE_URL}/_next/data/{BUILD_ID}/courses/{COURSE}/{FIRST_SLUG}.json"
resp = session.get(url, cookies=cookies, allow_redirects=False)

if resp.status_code != 200:
    print(f"ERROR: Could not fetch first chapter (HTTP {resp.status_code})")
    exit(1)

data = resp.json()
toc = data.get("pageProps", {}).get("toc", [])
if not toc:
    print("ERROR: No TOC found in response.")
    exit(1)

# Extract slugs from TOC
slugs = []
for entry in toc:
    slug_list = entry.get("slug", [])
    if slug_list:
        slugs.append(slug_list[0])
    elif entry.get("id"):
        slugs.append(entry["id"])

print(f"Found {len(slugs)} chapters:")
for i, slug in enumerate(slugs):
    title = next((e.get("title", slug) for e in toc if (e.get("slug", [None])[0] if e.get("slug") else e.get("id")) == slug), slug)
    print(f"  {i+1:02d}. {title}")

# Save the first chapter (already have data)
first_json_path = os.path.join(OUTPUT_DIR, f"01-{FIRST_SLUG}.json")
if not os.path.exists(first_json_path) and data.get("pageProps", {}).get("code"):
    with open(first_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\n[01/{len(slugs)}] Saved {FIRST_SLUG}")

# Step 3: Download all chapters
print(f"\nDownloading all chapters...")
failed = []
for idx, slug in enumerate(slugs, 1):
    num = f"{idx:02d}"
    json_path = os.path.join(OUTPUT_DIR, f"{num}-{slug}.json")

    if os.path.exists(json_path):
        print(f"[{num}/{len(slugs)}] Already have {slug}")
        continue

    print(f"[{num}/{len(slugs)}] Downloading {slug}...")
    url = f"{BASE_URL}/_next/data/{BUILD_ID}/courses/{COURSE}/{slug}.json"
    resp = session.get(url, cookies=cookies, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        if data.get("pageProps", {}).get("code"):
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print(f"  OK ({len(data['pageProps']['code'])} bytes)")
        else:
            print(f"  FAILED: no content (may need auth)")
            failed.append(slug)
    else:
        print(f"  FAILED: HTTP {resp.status_code}")
        failed.append(slug)

    time.sleep(0.3)

print(f"\nDone! Downloaded {len(slugs) - len(failed)}/{len(slugs)} pages")
if failed:
    print(f"Failed: {', '.join(failed)}")

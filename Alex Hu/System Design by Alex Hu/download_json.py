"""Download all raw JSON data from ByteByteGo course."""
import json
import os
import time
import requests

BASE_URL = "https://bytebytego.com"
BUILD_ID = "ne9ioqMiWrjC2OkKvGQqS"
COURSE = "system-design-interview"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw_json")
TOKEN = os.environ.get("BBG_TOKEN", "")

SLUGS = [
    "foreword",
    "join-discord-community",
    "scale-from-zero-to-millions-of-users",
    "back-of-the-envelope-estimation",
    "a-framework-for-system-design-interviews",
    "design-a-rate-limiter",
    "design-consistent-hashing",
    "design-a-key-value-store",
    "design-a-unique-id-generator-in-distributed-systems",
    "design-a-url-shortener",
    "design-a-web-crawler",
    "design-a-notification-system",
    "design-a-news-feed-system",
    "design-a-chat-system",
    "design-a-search-autocomplete-system",
    "design-youtube",
    "design-google-drive",
    "proximity-service",
    "nearby-friends",
    "google-maps",
    "distributed-message-queue",
    "metrics-monitoring-and-alerting-system",
    "ad-click-event-aggregation",
    "hotel-reservation-system",
    "distributed-email-service",
    "s3-like-object-storage",
    "real-time-gaming-leaderboard",
    "payment-system",
    "digital-wallet",
    "stock-exchange",
    "the-learning-continues",
]

os.makedirs(OUTPUT_DIR, exist_ok=True)
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

failed = []
for idx, slug in enumerate(SLUGS, 1):
    num = f"{idx:02d}"
    json_path = os.path.join(OUTPUT_DIR, f"{num}-{slug}.json")
    if os.path.exists(json_path):
        print(f"[{num}/{len(SLUGS)}] Already have {slug}")
        continue

    print(f"[{num}/{len(SLUGS)}] Downloading {slug}...")
    url = f"{BASE_URL}/_next/data/{BUILD_ID}/courses/{COURSE}/{slug}.json"
    cookies = {"token": TOKEN} if TOKEN else {}
    resp = session.get(url, cookies=cookies, allow_redirects=False)

    if resp.status_code != 200:
        # Try without auth
        resp = session.get(url, allow_redirects=False)

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

print(f"\nDone! Downloaded {len(SLUGS) - len(failed)}/{len(SLUGS)} pages")
if failed:
    print(f"Failed: {', '.join(failed)}")

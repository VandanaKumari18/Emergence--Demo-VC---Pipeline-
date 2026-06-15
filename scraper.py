import requests
import json
import re
from html import unescape

def clean_html(text):
    text = unescape(text)
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def fix_name(name):
    name = re.split(r'\s+(turns|is|helps|lets|makes|enables|allows|for|to)\s+', name)[0]
    return name.strip()

def extract_name(title):
    title = re.sub(r'^(Launch HN:|Show HN:)\s*', '', title)
    title = re.sub(r'\(YC W25\)\s*', '', title)
    title = re.split(r'[–\-]', title)[0]
    return fix_name(title.strip())

def scrape_yc_startups():
    url = "https://hn.algolia.com/api/v1/search?query=Launch+HN+YC+W25&tags=story&hitsPerPage=50"
    response = requests.get(url)
    data = response.json()

    startups = []
    for hit in data.get("hits", []):
        title = hit.get("title", "")
        story_text = hit.get("story_text", "") or ""
        cleaned_description = clean_html(story_text[:500]) if story_text else "N/A"
        startups.append({
            "name": extract_name(title),
            "description": cleaned_description,
            "website": hit.get("url", "N/A"),
            "hn_points": hit.get("points", 0),
            "hn_comments": hit.get("num_comments", 0),
            "author": hit.get("author", "N/A")
        })

    print(f"Found {len(startups)} startups")
    return startups

if __name__ == "__main__":
    startups = scrape_yc_startups()
    print(json.dumps(startups[:3], indent=2))

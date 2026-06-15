import os
import json
from scraper import scrape_yc_startups
from analyser import analyse_startup

def save_memo(startup_name, memo_text):
    os.makedirs("outputs", exist_ok=True)
    filename = startup_name.lower().replace(" ", "_").replace("/", "_")
    filepath = f"outputs/{filename}.md"
    with open(filepath, "w") as f:
        f.write(memo_text)
    print(f"Saved: {filepath}")

def run_pipeline(limit=10):
    print("Starting VC Deal Flow Pipeline...\n")
    startups = scrape_yc_startups()
    print(f"\nAnalysing top {limit} startups...\n")
    for i, startup in enumerate(startups[:limit]):
        print(f"Analysing {i+1}/{limit}: {startup['name']}")
        try:
            memo = analyse_startup(startup)
            save_memo(startup['name'], memo)
        except Exception as e:
            print(f"Failed for {startup['name']}: {e}")
    print("\nDone! All memos saved in outputs/ folder.")

if __name__ == "__main__":
    run_pipeline(limit=10)

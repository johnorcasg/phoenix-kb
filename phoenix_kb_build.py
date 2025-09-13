"""
Phoenix KB Build Script
Syncs Markdown KB files into a unified index for the web crawler.
"""

import os, json, yaml

KB_DIR = "./kb_files"
OUTPUT = "./phoenix_index.json"

def build_index():
    index = {"files": []}
    for root, _, files in os.walk(KB_DIR):
        for f in files:
            if f.endswith((".md", ".yml", ".json")):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                index["files"].append({"name": f, "path": path, "content": content})
    with open(OUTPUT, "w", encoding="utf-8") as out:
        json.dump(index, out, indent=2)

if __name__ == "__main__":
    build_index()
    print("Phoenix KB index built at", OUTPUT)

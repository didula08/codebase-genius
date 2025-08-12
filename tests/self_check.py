# tests/self_check.py
import json, os, pathlib
from agents.supervisor import run

def main(repo="https://github.com/pallets/click"):
    root = pathlib.Path(__file__).resolve().parents[1]
    os.chdir(root)
    idx = run(repo)
    docs = root / "docs"

    # Files exist?
    assert (docs / "map.json").exists(), "map.json not generated"
    assert (docs / "readme_summaries.json").exists(), "readme_summaries.json not generated"
    assert (docs / "analysis.json").exists(), "analysis.json not generated"

    # Files are valid JSON (not empty/broken)
    for name in ["map.json", "readme_summaries.json", "analysis.json"]:
        with open(docs / name, "r", encoding="utf-8") as f:
            json.load(f)

    print("✅ Self-check passed. Docs index at:", idx)

if __name__ == "__main__":
    main()

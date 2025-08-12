import re, pathlib, json
from pathlib import Path

def _split_headings(md: str):
    blocks = re.split(r'\n(?=(#+)\s)', md)
    out = []
    for i in range(1, len(blocks), 2):
        hashes, rest = blocks[i], blocks[i+1]
        title, *body = rest.split('\n', 1)
        out.append((len(hashes), title.strip(), body[0] if body else ""))
    return out

def readme_outline_and_summaries(repo_path: str):
    rd = Path(repo_path)/"README.md"
    if not rd.exists():
        return {"outline": [], "summaries": []}
    md = rd.read_text(encoding="utf-8", errors="ignore")
    sections = _split_headings(md)
    # "Decreasing percentage" rule: Intro keeps more detail; later keeps less
    ratios = [0.5, 0.35, 0.25, 0.2, 0.15]
    summaries = []
    for i,(lvl,title,txt) in enumerate(sections):
        r = ratios[min(i, len(ratios)-1)]
        words = txt.split()
        keep = max(1, int(len(words)*r))
        summaries.append({"title": title, "summary": " ".join(words[:keep])})
    Path("docs/readme_summaries.json").write_text(
        json.dumps({"outline":[t for _,t,_ in sections],"summaries":summaries}, indent=2),
        encoding="utf-8")
    return {"outline":[t for _,t,_ in sections], "summaries": summaries}

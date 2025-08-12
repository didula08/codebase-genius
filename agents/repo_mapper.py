from tools.fs_tools import iter_files
from pathlib import Path
import json, os
def build_map(repo_path: str):
    repo_path = str(Path(repo_path).resolve())
    files = [str(p) for p in iter_files(repo_path)]
    by_top = {}
    for f in files:
        rel = os.path.relpath(f, repo_path)
        top = rel.split(os.sep)[0]
        by_top.setdefault(top, []).append(rel)
    out = {"repo": repo_path, "top_folders": sorted(by_top.keys()), "files": files}
    Path("docs").mkdir(exist_ok=True)
    Path("docs/map.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    return out

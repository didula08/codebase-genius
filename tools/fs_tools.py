from pathlib import Path
import pathspec

def _load_gitignore(root: Path):
    gi = root/".gitignore"
    if gi.exists():
        return pathspec.PathSpec.from_lines("gitwildmatch", gi.read_text().splitlines())
    return None

def iter_files(root_dir: str):
    root = Path(root_dir)
    spec = _load_gitignore(root)
    for p in root.rglob("*"):
        if p.is_dir(): continue
        rel = p.relative_to(root)
        if spec and spec.match_file(str(rel)): continue
        yield p

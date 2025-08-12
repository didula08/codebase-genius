import ast, pathlib, json
from pathlib import Path
def analyze_python_file(path: pathlib.Path):
    try: tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception: return None
    funcs, classes, imports = [], [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef): funcs.append(node.name)
        elif isinstance(node, ast.ClassDef): classes.append(node.name)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", None)
            if mod: imports.append(mod)
    return {"file": str(path), "functions": funcs, "classes": classes, "imports": imports}
def deep_dive(repo_path: str):
    results = []
    for p in pathlib.Path(repo_path).rglob("*.py"):
        r = analyze_python_file(p)
        if r: results.append(r)
    Path("docs/analysis.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    return results

from pathlib import Path
def render(output_dir="docs"):
    out = Path(output_dir); out.mkdir(exist_ok=True)
    (out/"index.md").write_text("# Codebase Genius Docs`n- See map.json`n- See readme_summaries.json`n- See analysis.json", encoding="utf-8")
    return out/"index.md"

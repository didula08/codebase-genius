from tools.git_tools import clone
from agents.repo_mapper import build_map
from tools.summarizer import readme_outline_and_summaries
from agents.code_analyzer import deep_dive
from agents.docgenie import render
from pathlib import Path

def run(repo_url_or_path: str, work="workspace"):
    work = Path(work); work.mkdir(exist_ok=True)
    if repo_url_or_path.startswith("http"):
        repo_path = str(work/"repo")
        clone(repo_url_or_path, repo_path)
    else:
        repo_path = repo_url_or_path
    build_map(repo_path)
    readme_outline_and_summaries(repo_path)
    deep_dive(repo_path)
    index = render("docs")
    return str(index)

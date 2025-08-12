import sys, pathlib, argparse
# ensure project root on sys.path if user runs directly
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from agents.supervisor import run
def main():
    p = argparse.ArgumentParser()
    p.add_argument("repo", help="GitHub URL or local path")
    args = p.parse_args()
    print("Docs index:", run(args.repo))
if __name__ == "__main__":
    main()

import subprocess, os
def clone(url: str, dest: str):
    if os.path.exists(dest): return dest
    subprocess.check_call(["git", "clone", "--depth", "1", url, dest])
    return dest

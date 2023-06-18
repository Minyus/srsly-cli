from pathlib import Path


def upath(path):
    if isinstance(path, str) and path.startswith("~"):
        path = str(Path.home()) + path[1:]
    return path

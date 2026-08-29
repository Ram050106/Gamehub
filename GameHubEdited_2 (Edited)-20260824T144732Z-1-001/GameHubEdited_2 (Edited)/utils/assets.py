import os

# This points to the GameHubShru folder (where assets/, ui/, games/ live)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(ROOT_DIR)  # utils → GameHubShru

def asset(filename: str) -> str:
    """
    Returns absolute path to a file inside GameHubShru/assets/
    """
    return os.path.join(ROOT_DIR, "assets", filename)

import pathlib
import subprocess

from ._version import __version__ as __base_version__

TESTREPOCOMPUTING_SRC = pathlib.Path(__file__).parent
TESTREPOCOMPUTING_ROOT = TESTREPOCOMPUTING_SRC.parent.parent
TESTREPOCOMPUTING_TESTS = TESTREPOCOMPUTING_ROOT / "tests"
TESTREPOCOMPUTING_DOCS = TESTREPOCOMPUTING_ROOT / "docs"


def _git_suffix() -> str:
    """If we are in a git repo, we want to add the necessary information to the
    version string.

    This will return something along the lines of ``+gf0f18e6.dirty``.
    """
    # pylint: disable=broad-except
    kwargs = dict(cwd=TESTREPOCOMPUTING_ROOT, stderr=subprocess.DEVNULL)
    try:
        # Retrieve the git short sha to be appended to the base version string.
        args = ["git", "rev-parse", "--short", "HEAD"]
        sha = subprocess.check_output(args, **kwargs).decode().strip()
        suffix = f"+g{sha}"
        # If we have uncommitted changes, append a `.dirty` to the version suffix.
        args = ["git", "diff", "--quiet"]
        if subprocess.call(args, stdout=subprocess.DEVNULL, **kwargs) != 0:
            suffix = f"{suffix}.dirty"
        return suffix
    except Exception:
        return ""


__version__ = f"{__base_version__}{_git_suffix()}"
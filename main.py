"""Loading Screen Gold entry: one loading-screen tip, one line, <=200 chars.

Writes the tip to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, no network, deterministic.
"""

import os

TIP = (
    "Tip: your agent isn't frozen \u2014 it's reading the error you skipped. "
    "Grab coffee, check the logs, and let it finish before you hit restart."
)


def main() -> None:
    # Gate, enforced before writing: one line, at most 200 characters.
    assert "\n" not in TIP and len(TIP) <= 200, "tip must be one line of <=200 chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TIP.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

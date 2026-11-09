
#!/usr/bin/env python3
"""Build the GNU Info edition of Scientific Visualization."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build" / "info"
IMAGES = BUILD / "images"
RST = ROOT / "rst"


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def expand_rst(path: Path, stack: tuple[Path, ...] = ()) -> str:
    """Expand RST includes, keeping original sources unchanged."""
    path = path.resolve()

    if path in stack:
        raise ValueError(f"Circular RST inclusion: {path}")

    result = []
    pattern = re.compile(r"^\.\. include::\s+(.+?)\s*$")

    for line in path.read_text(encoding="utf-8").splitlines(
        keepends=True
    ):
        match = pattern.match(line.strip())

        if match:
            included = path.parent / match.group(1)
            result.append(expand_rst(included, (*stack, path)))
        elif ":raw-latex:" not in line:
            result.append(line)

    return "".join(result)


def prepare_rst() -> Path:
    """Create a standalone RST document for Pandoc."""
    source = expand_rst(RST / "main.rst")

    # LaTeX-only substitutions are not useful in GNU Info.
    source = source.replace("|newline|", "")
    source = source.replace("|newpage|", "")

    BUILD.mkdir(parents=True, exist_ok=True)
    output = BUILD / "book.rst"
    output.write_text(source, encoding="utf-8")
    return output



def find_image(name: str, suffix: str) -> Path | None:
    """Find an image using deterministic path resolution."""
    relative = Path(name).with_suffix(suffix)
    directories = (ROOT / "figures", ROOT / "images")

    # 1. Exact relative path.
    for directory in directories:
        candidate = directory / relative
        if candidate.is_file():
            return candidate

    # 2. Case-insensitive relative path.
    wanted = relative.as_posix().casefold()

    for directory in directories:
        if not directory.is_dir():
            continue

        candidates = sorted(
            p for p in directory.rglob("*")
            if p.is_file()
            and p.relative_to(directory).as_posix().casefold()
            == wanted
        )

        if len(candidates) == 1:
            return candidates[0]

    # 3. Filename-only fallback.
    # Accept only if there is exactly one matching file.
    candidates = []

    for directory in directories:
        if not directory.is_dir():
            continue

        candidates.extend(
            p for p in directory.rglob("*")
            if p.is_file()
            and p.name.casefold() == relative.name.casefold()
        )

    if len(candidates) == 1:
        return candidates[0]

    if len(candidates) > 1:
        paths = "\n".join(f"  {p}" for p in sorted(candidates))
        raise ValueError(
            f"Ambiguous image: {name}{suffix}\n{paths}"
        )

    return None


def prepare_images(texi: Path) -> int:
    """Create PNG assets and rewrite Texinfo image references."""
    content = texi.read_text(encoding="utf-8")
    pattern = re.compile(r"@image\{([^}\n]+)\}")

    converted = 0
    missing = []

    def replace(match: re.Match[str]) -> str:
        nonlocal converted

        fields = match.group(1).split(",")
        name = fields[0].strip()

        destination = IMAGES / f"{name}.png"
        destination.parent.mkdir(parents=True, exist_ok=True)

        # Prefer an exact path before trying filename-only fallbacks.
        relative = Path(name)

        exact_png = ROOT / "figures" / relative.with_suffix(".png")
        exact_pdf = ROOT / "figures" / relative.with_suffix(".pdf")

        if exact_png.is_file():
            source_png = exact_png
            source_pdf = None
        elif exact_pdf.is_file():
            source_png = None
            source_pdf = exact_pdf
        else:
            source_png = find_image(name, ".png")
            source_pdf = None if source_png else find_image(name, ".pdf")

        if source_png:
            shutil.copyfile(source_png, destination)
        elif source_pdf:
            run(
                "pdftoppm",
                "-f", "1",
                "-l", "1",
                "-singlefile",
                "-r", "150",
                "-png",
                str(source_pdf),
                str(destination.with_suffix("")),
            )
        else:
            missing.append(name)
            return match.group(0)

        converted += 1
        return f"@image{{images/{name}}}"

    content = pattern.sub(replace, content)

    if missing:
        raise FileNotFoundError(
            "Missing images:\n" + "\n".join(sorted(set(missing)))
        )

    texi.write_text(content, encoding="utf-8")
    return converted


def main() -> None:
    for executable in ("pandoc", "makeinfo", "pdftoppm"):
        if not shutil.which(executable):
            raise RuntimeError(f"Missing executable: {executable}")

    rst = prepare_rst()
    texi = BUILD / "book.texi"
    output = BUILD / "scientific-visualization.info"

    run(
        "pandoc",
        "--from=rst",
        "--to=texinfo",
        "--standalone",
        "--metadata",
        "title=Scientific Visualization: Python + Matplotlib",
        "--output", str(texi),
        str(rst),
    )

    run(
        sys.executable,
        str(ROOT / "scripts" / "fix_texinfo_nodes.py"),
        str(texi),
    )

    # Discard stale generated images.
    if IMAGES.exists():
        shutil.rmtree(IMAGES)

    count = prepare_images(texi)

    run(
        "makeinfo",
        "--no-split",
        "--output", str(output),
        str(texi),
    )

    print(f"Built: {output.relative_to(ROOT)}")
    print(f"Images: {count}")
    print(f"Size: {output.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()

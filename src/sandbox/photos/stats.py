import sys
from pathlib import Path

from PIL import Image

IMAGE_DIR = Path(__file__).parent / "images"
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif"}


def list_images(directory: Path) -> list[Path]:
    """Return the image files in a directory, sorted by name."""
    if not directory.is_dir():
        return []
    return sorted(p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES)


def find_image(images: list[Path], name: str) -> Path | None:
    """Find an image by file name (case-insensitive), or return None."""
    wanted = name.strip().lower()
    for image in images:
        if image.name.lower() == wanted:
            return image
    return None


def load_image(path: Path) -> Image.Image:
    """Load an image file and return it as an RGB image."""
    with Image.open(path) as img:
        return img.convert("RGB")


def clear_red(img: Image.Image) -> Image.Image:
    """Return a copy of an RGB image with the red channel set to 0."""
    _, g, b = img.split()
    zero_red = Image.new("L", img.size, 0)
    return Image.merge("RGB", (zero_red, g, b))


def prompt_for_image(images: list[Path]) -> Path | None:
    """List the images and ask the user to pick one by name. None means quit."""
    print("Available images:")
    for image in images:
        print(f"  {image.name}")

    while True:
        choice = input("Enter an image name (or 'q' to quit): ")
        if choice.strip().lower() == "q":
            return None
        selected = find_image(images, choice)
        if selected is not None:
            return selected
        print(f"No image named '{choice.strip()}'. Try again.")


def main() -> int:
    images = list_images(IMAGE_DIR)
    if not images:
        print(f"No images found in {IMAGE_DIR.resolve()}")
        return 1

    selected = prompt_for_image(images)
    if selected is None:
        return 0

    img = load_image(selected)
    result = clear_red(img)

    output = selected.with_name(f"{selected.stem}_processed.png")
    result.save(output)
    print(f"Saved {output}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

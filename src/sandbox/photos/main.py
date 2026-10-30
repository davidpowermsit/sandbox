import sys
from pathlib import Path

from sandbox.photos.stats import clear_red, list_images, load_image, prompt_for_image

IMAGE_DIR = Path(__file__).parent / "images"
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif"}


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

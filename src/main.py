import os
import shutil
import sys

from copier import copy_static_to_public
from pagegen import generate_pages_recursive

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    base_path = base_path.rstrip("/")  # Prevent double slashes or newline issues

    output_dir = "docs"  # GitHub Pages requires output in the /docs folder

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    copy_static_to_public(output_dir)
    generate_pages_recursive("content", "template.html", output_dir, base_path)

    print("Site build complete!")

if __name__ == "__main__":
    main()

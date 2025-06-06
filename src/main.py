import sys
import shutil
import os
from copier import copy_static_to_public
from pagegen import generate_pages_recursive
from generate_page import generate_page  # ← manually call for root index.md

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    base_path = base_path.rstrip("/")

    output_dir = "docs"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    copy_static_to_public(output_dir)

    # Manually generate the homepage
    generate_page("content/index.md", "template.html", f"{output_dir}/index.html", base_path)

    # Recursively generate other pages
    generate_pages_recursive("content", "template.html", output_dir, base_path)

    print("Site build complete!")

if __name__ == "__main__":
    main()

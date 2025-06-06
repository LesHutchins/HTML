import os
from generate_page import generate_page

def generate_pages_recursive(content_dir, template_path, dest_dir, base_path="/"):
    for root, _, files in os.walk(content_dir):
        for filename in files:
            if not filename.endswith(".md"):
                continue

            src_md_path = os.path.join(root, filename)
            rel_path = os.path.relpath(src_md_path, content_dir)
            rel_path_no_ext = os.path.splitext(rel_path)[0]

            # Special case: content/index.md → docs/index.html
            if rel_path_no_ext == "index":
                dest_html_path = os.path.join(dest_dir, "index.html")
            else:
                dest_dir_path = os.path.join(dest_dir, rel_path_no_ext)
                os.makedirs(dest_dir_path, exist_ok=True)
                dest_html_path = os.path.join(dest_dir_path, "index.html")

            generate_page(src_md_path, template_path, dest_html_path, base_path)

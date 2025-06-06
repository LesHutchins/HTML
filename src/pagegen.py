import os
from markdown_converter import markdown_to_html_node
from extractor import extract_title
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if not file.endswith(".md"):
                continue

            src_md_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_md_path, dir_path_content)
            rel_path_no_ext = os.path.splitext(rel_path)[0]

            # Skip regenerating the homepage
            if rel_path_no_ext == "index":
                continue

            if rel_path_no_ext.endswith("/index"):
                rel_path_no_ext = rel_path_no_ext[:-len("/index")]

            dest_dir = os.path.join(dest_dir_path, rel_path_no_ext)
            dest_html_path = os.path.join(dest_dir, "index.html")

            os.makedirs(dest_dir, exist_ok=True)
            generate_page(src_md_path, template_path, dest_html_path, base_path)

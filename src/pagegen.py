import os
from markdown_converter import markdown_to_html_node
from extractor import extract_title

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} with base path {base_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    # Apply base path to relative URLs
    base_path = base_path.rstrip("/")  # prevent trailing slashes
    html = html.replace('href="/', f'href="{base_path}/')
    html = html.replace('src="/', f'src="{base_path}/')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path="/"):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if not file.endswith(".md"):
                continue

            src_md_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_md_path, dir_path_content)
            rel_path_no_ext = os.path.splitext(rel_path)[0]

            dest_dir = os.path.join(dest_dir_path, rel_path_no_ext)
            dest_html_path = os.path.join(dest_dir, "index.html")

            os.makedirs(dest_dir, exist_ok=True)
            generate_page(src_md_path, template_path, dest_html_path, base_path)

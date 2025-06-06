import os
from markdown_converter import markdown_to_html_node
from extractor import extract_title

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    # Patch absolute paths to include the GitHub base path
    html = html.replace('href="/', f'href="{base_path}/')
    html = html.replace('src="/', f'src="{base_path}/')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(html)

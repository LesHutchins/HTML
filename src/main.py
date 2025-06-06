def main():
    output_dir = "docs"  # <-- this should be "docs" for GitHub Pages
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    copy_static_to_public(output_dir)
    generate_pages_recursive("content", "template.html", output_dir, base_path)

import shutil
import os

def copy_static_to_public(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    shutil.copy("static/index.css", os.path.join(output_dir, "index.css"))

    static_images_dir = "static/images"
    if os.path.exists(static_images_dir):
        output_images_dir = os.path.join(output_dir, "images")
        shutil.copytree(static_images_dir, output_images_dir, dirs_exist_ok=True)

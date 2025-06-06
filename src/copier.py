import os
import shutil

def copy_static_to_public(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    shutil.copy("index.css", os.path.join(output_dir, "index.css"))

    if os.path.exists("images"):
        shutil.copytree("images", os.path.join(output_dir, "images"), dirs_exist_ok=True)

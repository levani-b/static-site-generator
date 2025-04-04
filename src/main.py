import sys
import os
import shutil

from copystatic import copy_files_recursive
from generate_content import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
basepath = sys.argv[1] if len(sys.argv) > 1 else '/'


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)
    


main()

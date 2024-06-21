#!/usr/bin/env python3
# from textnode import TextNode
import os
import shutil

from markdown import extract_title, markdown_to_htmlnode
from page import (
    generate_page_recursive,
    recursive_delete_items,
    recursive_list_items,
)


if __name__ == "__main__":
    if os.path.exists("public"):
        recursive_delete_items("public")
    else:
        os.mkdir("public")

    arr = []
    arr = recursive_list_items("static", arr)
    for item in arr:
        src = "static/" + item
        dst = "public/" + item
        if len(item.split("/")) > 1:
            os.mkdir("/".join(dst.split("/")[:-1]))
        print(f"copying {src} to {dst}")
        shutil.copy(src, dst)

    generate_page_recursive("content", "template.html", "public")

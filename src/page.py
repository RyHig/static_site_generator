#!/usr/bin/env python3

from markdown import extract_title, markdown_to_htmlnode
import os


def recursive_delete_items(directory):
    for item in os.listdir(directory):
        relative_path = directory + "/" + item
        if os.path.isdir(relative_path):
            recursive_delete_items(relative_path)
            print(f"Removing dir: {relative_path}")
            os.rmdir(relative_path)
        else:
            print(f"Removing file: {relative_path}")
            os.remove(relative_path)


def recursive_list_items(directory, arr):
    for item in os.listdir(directory):
        relative_path = directory + "/" + item
        if os.path.isdir(relative_path):
            recursive_list_items(relative_path, arr)
        else:
            split = relative_path.split("/")
            arr.append("/".join(split[1:]))
    return arr


def generate_page(from_path, template_path, dest_path):

    print(
        f"Generating a page from {from_path} to {dest_path} using {template_path} as a template"
    )
    with open(from_path) as f:
        markdown = "".join(f.readlines())
        f.close()

    with open(template_path) as f:
        template = "".join(f.readlines())
        f.close()

    title = extract_title(markdown)
    content = markdown_to_htmlnode(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content.to_html())
    os.makedirs("/".join(dest_path.split("/")[:-1]), exist_ok=True)
    with open(dest_path, "x") as f:
        f.write(template)
        f.flush()
        f.close()


def generate_page_recursive(dir_from_path, template_path, dir_dest_path):
    for item in os.listdir(dir_from_path):
        relative_path = dir_from_path + "/" + item
        if os.path.isdir(relative_path):
            generate_page_recursive(relative_path, template_path, dir_dest_path)
        else:
            dest_file = "/".join(
                [dir_dest_path] + relative_path.split("/")[1:-1] + ["index.html"]
            )
            generate_page(relative_path, template_path, dest_file)

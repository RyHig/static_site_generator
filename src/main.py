#!/usr/bin/env python3
# from textnode import TextNode
import os
import shutil


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

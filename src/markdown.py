#!/usr/bin/env python3


def markdown_to_blocks(markdown):
    split = markdown.split("\n")
    new_list = []
    block = []
    for line in split:
        line = line.strip()
        if line == "":
            new_list.append(block)
            block = []
            continue
        block.append(line)
    if block != []:
        new_list.append(block)
    return new_list


def block_to_block_type(block):
    if block[0].startswith("#"):
        stripped = block[0].strip("#")
        if stripped.startswith(" "):
            return "heading"
        return "paragraph"
    elif block[0].startswith("```") and block[-1].endswith("```"):
        return "code"
    elif block[0].startswith(">"):
        for b in block:
            if not b.startswith(">"):
                return "paragraph"
        return "quote"
    elif block[0].startswith("* ") or block[0].startswith("- "):
        for b in block:
            if not b.startswith("* ") and not b.startswith("- "):
                return "paragraph"
        return "unordered_list"
    elif block[0][0] == "1" and (block[0][1:3] == ". "):
        num = 2
        for b in block:
            if block[0][0] != str(num) and (block[0][1:3] != ". "):
                return "paragraph"
        return "ordered_list"

    return "paragraph"

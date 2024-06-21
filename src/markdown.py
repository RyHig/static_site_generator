#!/usr/bin/env python3


from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_html_node, text_to_textnodes


def markdown_to_blocks(markdown):
    split = markdown.split("\n")
    new_list = []
    block = []
    for line in split:
        line = line.strip()
        if line == "":
            if block == []:
                continue
            new_list.append(block)
            block = []
        elif line.startswith("#"):
            if block != []:
                new_list.append(block)
                block = []
            new_list.append([line])
        else:
            block.append(line)
    if block != []:
        new_list.append(block)
    return new_list


def block_to_block_type(block):
    if block[0].startswith("#"):
        stripped = block[0].strip("#")
        if stripped.startswith(" "):
            count = block[0].count("#")
            if count > 6:
                return "paragraph"
            return "h" + str(count)
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


def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    blocktypes = [block_to_block_type(block) for block in blocks]
    leafnodes = []
    for i in range(len(blocktypes)):
        tag = None
        match blocktypes[i]:
            case "paragraph":
                leafnodes.append(paragraph_parse_delimiters(" ".join(blocks[i])))
            case "quote":
                quote_string = ""
                for line in blocks[i]:
                    quote_string += line[1:]
                leafnodes.append(LeafNode("blockquote", quote_string))
            case "unordered_list":
                orderedlist = []
                for line in blocks[i]:
                    orderedlist.append(LeafNode("li", line[2:]))
                leafnodes.append(ParentNode("ul", orderedlist))
            case "ordered_list":
                tag = "ol"
                orderedlist = []
                for line in blocks[i]:
                    orderedlist.append(LeafNode("li", line[3:]))
                leafnodes.append(ParentNode("ol", orderedlist))
            case "code":
                tag = "code"
                block_string = " ".join(blocks[i]).strip("` ")
                leafnodes.append(ParentNode("pre", [LeafNode(tag, block_string)]))
            case _:
                string = "".join(blocks[i]).strip("# ")
                leafnodes.append(LeafNode(blocktypes[i], string))
    return ParentNode("div", leafnodes)


def paragraph_parse_delimiters(paragraph):
    textnodes = text_to_textnodes(paragraph)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return ParentNode("p", children)

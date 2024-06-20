#!/usr/bin/env python3

from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        if self.text != value.text:
            return False
        if self.text_type != value.text_type:
            return False
        if self.url != value.url:
            return False
        return True

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "image":
            return LeafNode(
                "img", "", props={"src": text_node.url, "alt": text_node.text}
            )
        case "link":
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case _:
            raise Exception("case not handled.")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        split = node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise ValueError

        for i in range(len(split)):
            if i % 2 != 0:
                new_nodes.append(TextNode(split[i], text_type))
            else:
                new_nodes.append(TextNode(split[i], "text"))
    return new_nodes

#!/usr/bin/env python3
# from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, split_nodes_delimiter, text_node_to_html_node

if __name__ == "__main__":
    node = HTMLNode("b", "value")
    print(node)
    hmm = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(hmm.to_html())
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")
    print(new_nodes)
    for i in new_nodes:
        html_node = text_node_to_html_node(i).to_html()
        print(html_node)

#!/usr/bin/env python3
# from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import block_to_block_type, markdown_to_blocks
from textnode import (
    TextNode,
    split_nodes_delimiter,
    split_nodes_links,
    text_node_to_html_node,
    split_nodes_image,
    text_to_textnodes,
)


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
    node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        "text",
    )
    print(split_nodes_image([node]))
    node = TextNode(
        "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another).",
        "text",
    )
    print(split_nodes_links([node]))
    test = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(test)
    print(nodes)

    lines = """This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
    This is the same paragraph on a new line

    ## asd

    # 123412

    ##### 123412

    1. b
    2. a
    3. c

    10. 123
    11. 1234

    > asd
    > asd

    ```
    asdasdqwe
    qasdwqeqwe
    qweqasd
    ```

    - a
    * This is a list
    * with items"""
    blocks = markdown_to_blocks(lines)

    print(blocks)
    l = []
    for block in blocks:
        l.append(block_to_block_type(block))
    blocks = markdown_to_blocks(lines)
    print(l)

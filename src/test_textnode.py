#!/usr/bin/env python3
import unittest

from textnode import (
    TextNode,
    extract_markdown_image,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_links,
    text_node_to_html_node,
    text_to_textnodes,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_textnode_to_htmlnode(self):
        node = TextNode("This is a text node", "text")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.to_html(), "This is a text node")

        node = TextNode("This is a text node", "bold")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.to_html(), "<b>This is a text node</b>")

        node = TextNode("This is a text node", "italic")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.to_html(), "<i>This is a text node</i>")

        node = TextNode("This is a text node", "code")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.to_html(), "<code>This is a text node</code>")

        node = TextNode("This is a text node", "link", "https://www.google.com")
        leaf = text_node_to_html_node(node)
        self.assertEqual(
            leaf.to_html(), '<a href="https://www.google.com">This is a text node</a>'
        )

        node = TextNode("This is a text node", "image", "https://www.google.com")
        leaf = text_node_to_html_node(node)
        self.assertEqual(
            leaf.to_html(),
            '<img src="https://www.google.com" alt="This is a text node"></img>',
        )

        node = TextNode("This is a text node", "c")
        self.assertRaises(Exception, text_node_to_html_node, node)

    def test_node_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")

        node_array = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, node_array)

        node = TextNode("This is text with a *code block* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        node_array = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "italic"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, node_array)

        node = TextNode("This is text with a **code block** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        node_array = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "bold"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, node_array)

    def test_extract_image(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)\
        and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        matches = extract_markdown_image(text)
        expect = [
            (
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            (
                "another",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
            ),
        ]
        self.assertEqual(matches, expect)

    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)."
        matches = extract_markdown_links(text)
        expect = [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another"),
        ]
        self.assertEqual(matches, expect)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
        )
        nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with an ", "text"),
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text"),
            TextNode(
                "second image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another).",
            "text",
        )
        nodes = split_nodes_links([node])
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("link", "link", "https://www.example.com"),
            TextNode(" and ", "text"),
            TextNode("another", "link", "https://www.example.com/another"),
            TextNode(".", "text"),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_all_text(self):

        test = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(test)
        expected = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected)


if __name__ == "__main__":
    unittest.main()

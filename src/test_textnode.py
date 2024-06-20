#!/usr/bin/env python3
import unittest

from textnode import TextNode, split_nodes_delimiter, text_node_to_html_node


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


if __name__ == "__main__":
    unittest.main()

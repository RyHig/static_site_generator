#!/usr/bin/env python3
import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )


class TestLeafNode(unittest.TestCase):
    def test_tag(self):
        node = LeafNode("a", "Blah blah")
        self.assertEqual(node.to_html(), "<a>Blah blah</a>")

    def test_tag_props(self):
        node = LeafNode("a", "Blah blah", props={"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Blah blah</a>'
        )

    def test_props(self):
        node = LeafNode(None, "Blah blah", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "Blah blah")

    def test_no_value(self):
        node = LeafNode(None, None, props={"href": "https://www.google.com"})
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()

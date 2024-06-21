#!/usr/bin/env python3

import unittest

from markdown import block_to_block_type, markdown_to_blocks, markdown_to_htmlnode


class TestMarkdown(unittest.TestCase):
    def test_markdown_to_block(self):

        lines = """This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items"""

        blocks = markdown_to_blocks(lines)
        expected = [
            ["This is **bolded** paragraph"],
            [
                "This is another paragraph with *italic* text and `code` here",
                "This is the same paragraph on a new line",
            ],
            ["* This is a list", "* with items"],
        ]
        self.assertEqual(blocks, expected)
        expected = [
            ["This is **bolded** paragraph"],
            [
                "This is another paragraph with *italic* text and `code` here",
            ],
            ["* This is a list", "* with items"],
        ]
        self.assertNotEqual(blocks, expected)

    def test_block_to_blocktypes(self):
        lines = """This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        >
        >


        1. b
        2. c

        ##### 1

        * This is a list
        * with items"""

        blocktypes = [block_to_block_type(block) for block in markdown_to_blocks(lines)]

        expected = [
            "paragraph",
            "paragraph",
            "quote",
            "ordered_list",
            "h5",
            "unordered_list",
        ]
        self.assertEqual(blocktypes, expected)

    def test_markdown_to_htmlnode(self):
        lines = """### Blah
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        ```
        blah blah blah
        ```

        >
        >


        1. b
        2. c

        ##### 1

        * This is a list
        * with items"""
        expected = [
            "h3",
            "paragraph",
            "paragraph",
            "quote",
            "ordered_list",
            "h5",
            "unordered_list",
        ]
        self.assertFalse(markdown_to_htmlnode(lines).to_html())

#!/usr/bin/env python3

import unittest

from markdown import markdown_to_blocks


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

import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from utils import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_three_spaces(self):
        text = "First block \n\n\nSecond block"
        expected_result = ["First block", "Second block"]
        text = markdown_to_blocks(text)
        self.assertListEqual(text,expected_result)

    def test_one_spaces(self):
        text = "First block \nSecond block"
        expected_result = ["First block \nSecond block"]
        text = markdown_to_blocks(text)
        self.assertListEqual(text,expected_result)

    def test_multiple_blocks(self):
        text = """# This is a heading
This is a paragraph of text.

* First item
* Second item

Last paragraph"""
        expected_result = [
            "# This is a heading\nThis is a paragraph of text.",
            "* First item\n* Second item",
            "Last paragraph"
        ]
        result = markdown_to_blocks(text)
        self.assertListEqual(result, expected_result)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


if __name__ == "__main__":
    unittest.main()
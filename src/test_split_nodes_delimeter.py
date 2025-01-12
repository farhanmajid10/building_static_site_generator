import unittest
from textnode import TextType, TextNode
from htmlnode import HTMLNode,ParentNode,LeafNode
from utils import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_normal(self):
        one = TextNode("I am *king*.", TextType.TEXT)
        two = TextNode("*I am Knight.*", TextType.BOLD)
        three = TextNode("I am *Igris*.", TextType.TEXT)
        somelist = [one,two,three]
        result = split_nodes_delimiter(somelist, "*", TextType.BOLD)
        uno = TextNode("I am ", TextType.TEXT)
        dos = TextNode("king", TextType.BOLD)
        tres = TextNode(".", TextType.TEXT)
        quatro = TextNode("*I am Knight.*", TextType.BOLD)
        cinco = TextNode("I am ", TextType.TEXT)
        seis = TextNode("Igris", TextType.BOLD)
        siete = TextNode(".", TextType.TEXT)
        templist = [uno,dos,tres,quatro,cinco,seis,siete]
        self.assertListEqual(result, templist)

    def test_empty_list(self):
        result = split_nodes_delimiter([], "*", TextType.BOLD)
        self.assertListEqual(result, [])

    def test_no_delimiters_present(self):
        node = TextNode("plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertListEqual(result, [node])

    def test_unmatched_delimiter(self):
        node = TextNode("I am *king* of the *world.", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.BOLD)

    def test_multiple_delimiters(self):
        node = TextNode("I am *king* of the *world*.", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        one = TextNode("I am ", TextType.TEXT)
        two = TextNode("king", TextType.BOLD)
        three = TextNode(" of the ", TextType.TEXT)
        four = TextNode("world", TextType.BOLD)
        five = TextNode(".", TextType.TEXT)
        tempcomp = [one,two,three,four,five]
        self.assertListEqual(result,tempcomp)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
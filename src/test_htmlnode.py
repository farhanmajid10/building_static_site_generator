from htmlnode import HTMLNode, LeafNode

import unittest

#from .textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_html_equality(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node.value,node2.value)

    def test_node_value_equality(self):
        node = HTMLNode("p", "some value")
        node2 = HTMLNode("c","some value")
        self.assertEqual(node.value, node2.value)

    def test_node_tag_value(self):
        node = HTMLNode("p", "smoe")
        node2 = HTMLNode("r", "dfs")
        self.assertNotEqual(node.tag, node2.tag)

    def test_leafnode(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leafnode(self):
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")


if __name__ == "__main__":
    unittest.main()
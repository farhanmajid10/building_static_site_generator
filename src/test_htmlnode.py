import unittest

from htmlnode import HTMLNode

from .textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_html_equality(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node,node2)

    def test_node_value_equality(self):
        node = HTMLNode("p", "some value")
        node2 = HTMLNode("c","some value")
        self.assertEqual(node.value, node2.value)

    def test_node_tag_value(self):
        node = HTMLNode("p", "smoe")
        node2 = HTMLNode("r", "dfs")
        self.assertNotEqual(node.tag, node2.tag)


if __name__ == "__main__":
    unittest.main()
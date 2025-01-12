import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode,LeafNode
from utils import text_node_to_html_node

class TestTextNodeConverter(unittest.TestCase):
    def test_bold(self):
        result = TextNode(text="just a test.", text_type=TextType.BOLD)
        result = text_node_to_html_node(result)
        temp = LeafNode(tag="b",value="just a test.")
        self.assertEqual(result.to_html(), temp.to_html())

    def test_link(self):
        result = TextNode(text="some rand text.", text_type=TextType.LINK, url="https//:somepage")
        result = text_node_to_html_node(result)
        temp = LeafNode(tag="a",value="some rand text.", props={"href":"https//:somepage"})
        self.assertEqual(result.to_html(),temp.to_html())

    def test_url(self):
        result = TextNode(text="could not load image.", text_type=TextType.IMAGE, url = "www.image.com")
        result = text_node_to_html_node(result)
        temp = LeafNode(tag="img", value="", props={"src": "www.image.com", "alt":"could not load image."})
        self.assertEqual(result.to_html(), temp.to_html())
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()
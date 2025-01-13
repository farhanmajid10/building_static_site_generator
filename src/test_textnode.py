import unittest

from textnode import TextNode, TextType
from utils import text_to_textnodes

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)
    
    def test_type_equality(self):
        node = TextNode("Test text", TextType.TEXT)
        node2 = TextNode("test text", TextType.TEXT)
        self.assertEqual(node.text_type.value, node2.text_type.value)
        
    def test_text_equality(self):
        node = TextNode("some", TextType.BOLD)
        node2 = TextNode("some", TextType.CODE)
        self.assertEqual(node.text, node2.text)

    def test_url_default(self):
        node = TextNode("some", TextType.BOLD)
        node2 = TextNode("so", TextType.ITALIC)
        self.assertEqual(node.url, node2.url)
    
    def test_text_inequality(self):
        node = TextNode("some", TextType.CODE)
        node2 = TextNode("sot", TextType.IMAGE)
        self.assertNotEqual(node.text, node2.text)
    
    def text_type_inequality(self):
        node = TextNode("some", TextType.BOLD)
        node2 = TextNode("some", TextType.CODE)
        self.assertNotEqual(node.text_type.value, node2.text_type.value)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node = TextNode(text,TextType.TEXT)
        result = text_to_textnodes(node)
        self.assertListEqual(result, (
           [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ] 
        ))

    



if __name__ == "__main__":
    unittest.main()
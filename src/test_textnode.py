import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)
    
    def test_type_equality(self):
        node = TextNode("Test text", TextType.NORMAL)
        node2 = TextNode("test text", TextType.NORMAL)
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
        node2 = TextNode("sot", TextType.IMAGES)
        self.assertNotEqual(node.text, node2.text)
    
    def text_type_inequality(self):
        node = TextNode("some", TextType.BOLD)
        node2 = TextNode("some", TextType.CODE)
        self.assertNotEqual(node.text_type.value, node2.text_type.value)

if __name__ == "__main__":
    unittest.main()
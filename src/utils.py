from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            result = LeafNode(tag=None,value=text_node.text)
            return result
        case TextType.BOLD:
            result = LeafNode(tag="b",value=text_node.text)
            return result
        case TextType.ITALIC:
            result = LeafNode(tag="i",value=text_node.text)
            return result
        case TextType.CODE:
            result = LeafNode(tag="code",value=text_node.text)
            return result
        case TextType.LINK:
            result = LeafNode(tag="a",value=text_node.text, props={"href":text_node.url})
            return result
        case TextType.IMAGE:
            result = LeafNode(tag="img",value="",props={"src" :text_node.url, "alt" : text_node.text})
            return result
        case _: 
            raise Exception("Texttype wrong.")
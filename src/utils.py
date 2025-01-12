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
        
def split_nodes_delimiter(old_nodes, delimeter,text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        chunk = node.text.split(f"{delimeter}")
        if len(chunk) == 1:
            new_nodes.append(TextNode(chunk[0],TextType.TEXT))
            continue
        if len(chunk) % 2 == 0:
            raise Exception("Invalid markdown, formatted section not closed")
        for i in range(len(chunk)):
            if chunk[i] == "":
                continue
            if i % 2 == 0:
                temp = TextNode(chunk[i], TextType.TEXT)
                new_nodes.append(temp)
            else:
                temp = TextNode(chunk[i], text_type)
                new_nodes.append(temp)
    return new_nodes
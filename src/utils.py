from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
import re

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

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        img_list = extract_markdown_images(node.text)
        if len(img_list) == 0:
            new_nodes.append(node)
        if len(img_list) > 0:
            remaining = node.text
            for img in img_list:
                alt_text, url = img
                full_img = f"![{alt_text}]({url})"
                temp = remaining.split(full_img,1)
                if temp[0]:
                    new_node = TextNode(temp[0],TextType.TEXT)
                    new_nodes.append(new_node)

                new_node = TextNode(alt_text,TextType.IMAGE,url)
                new_nodes.append(new_node)
                if len(temp) > 1:
                    remaining = temp[1]
                else:
                    remaining = ""
            if remaining:
                new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        img_list = extract_markdown_links(node.text)
        if len(img_list) == 0:
            new_nodes.append(node)
        if len(img_list) > 0:
            remaining = node.text
            for img in img_list:
                text, url = img
                full_img = f"[{text}]({url})"
                temp = remaining.split(full_img,1)
                if temp[0]:
                    new_node = TextNode(temp[0],TextType.TEXT)
                    new_nodes.append(new_node)

                new_node = TextNode(text,TextType.LINK,url)
                new_nodes.append(new_node)
                if len(temp) > 1:
                    remaining = temp[1]
                else:
                    remaining = ""
            if remaining:
                new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    result = split_nodes_delimiter([text], "**",TextType.BOLD)
    result = split_nodes_delimiter(result,"*", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result

def markdown_to_blocks(markdown):
    blocks = re.split(r"\n\n+",markdown)
    # + means more of what came before.

    result = []
    for block in blocks:
        cblock = block.strip()
        if cblock:
            result.append(cblock)
    return result

from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


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

def block_to_block_type(block):
    if block[0] == "#":
        temp_block = block.lstrip("#")
        num_of_hashes = len(block) - len(temp_block)
        if num_of_hashes <= 6:    
            if(block[num_of_hashes] == " "):
                return block_type_heading
    if block[0] == "`":
        if block.startswith("```") and block.endswith("```"):
            return block_type_code
    if block.startswith("> "):
        b_lines = block.split("\n")
        counter = 0
        for line in b_lines:
            if(line.startswith("> ")):
                counter += 1
        if counter == len(b_lines):
            return block_type_quote
    if block.startswith("* ") or block.startswith("- "):
        block_lines = block.split("\n")
        counter = 0
        for blck in block_lines:
            if blck.startswith(block[0:2]):
                counter += 1
        if counter == len(block_lines):
            return block_type_ulist
    if block.startswith("1. "):
        counter = 1
        bl_lines = block.split("\n")
        for blck in bl_lines:
            if (". ") in blck:
                temp_blck = blck.split(". ",1)#used maxsplit to only do the correct split.
                if(len(temp_blck) != 2 or not temp_blck[0].isdigit()):
                    return block_type_paragraph
                if int(temp_blck[0]) != counter:
                    return block_type_paragraph
                counter += 1
            else: 
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph
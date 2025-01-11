from textnode import TextNode, TextType
from functools import reduce

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result_ = ""
        if not self.props:
            return result_
        for key, value in self.props.items():
            result_ += " " + key + "=" + "\"" + value + "\""
        return result_
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None,  props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.tag == "img":
            if not self.props or "src" not in self.props or "alt" not in self.props:
                raise ValueError("Image tags require 'src' and 'alt' properties")
            return f"<{self.tag}{self.props_to_html}/>"
        if self.tag == "a":
            if not self.props or "href" not in self.props:
                raise ValueError("Anchor tags require 'href' property")
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        result = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return result
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tags.")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")

        result = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"           

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
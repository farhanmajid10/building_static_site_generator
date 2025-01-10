from textnode import TextNode, TextType

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
            result_ += " " + key + "=" + value
        return result_
    
    def __repr__(self):
        return f" tag: {self.tag}\n value: {self.value} \n props: \n {self.props_to_html()} \n children: {self.value}"
    

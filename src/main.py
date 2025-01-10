from textnode import TextNode, TextType
from htmlnode import LeafNode,HTMLNode
def main():
    some_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")

    some_node = LeafNode("p", "This is a paragraph of text.")
    print(some_node.to_html())
    some_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(some_node.to_html())
    #print(some_node)

if __name__ == "__main__":
    main()
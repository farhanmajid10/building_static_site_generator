from textnode import TextNode, TextType

def main():
    some_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")

    print(some_node)

if __name__ == "__main__":
    main()
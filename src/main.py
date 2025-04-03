from textnode import TextNode, TextType

def main():
    node1 = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    node = TextNode('text with _italic_ word', TextType.TEXT)


main()
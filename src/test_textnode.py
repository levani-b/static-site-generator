import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.ITALIC)
        self.assertNotEqual(node,node2)
    
    def test_eq_false2(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node2', TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_eq_with_link(self):
        node = TextNode('This is a text node', TextType.LINK, 'google.com')
        node2 = TextNode('This is a text node', TextType.LINK, 'google.com')
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode('This is a text node', TextType.LINK, 'google.com')
        self.assertEqual(repr(node), 'TextNode(This is a text node, link, google.com)')
    
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "image"},
        )

if __name__ == '__main__':
    unittest.main()
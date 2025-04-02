import unittest

from textnode import TextNode, TextType

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

if __name__ == '__main__':
    unittest.main()
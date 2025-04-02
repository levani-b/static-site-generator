import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    # tests for html node
    def test_to_html_props(self):
        node = HTMLNode('div', 'HEY YOU!', None, { "href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_different_values(self):
        node = HTMLNode('div', "HEY YOU!")
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, "HEY YOU!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode('div', 'HEY YOU', None, {"href": 'google.com'})
        self.assertEqual(
            repr(node),
            "HTMLNode(div, HEY YOU, children: None, {'href': 'google.com'})"
        )

    def test_when_props_none(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            None
        )
        self.assertEqual(node.props_to_html(),
            "",)


    # tests for leaf node

    def test_leaf_to_html_with_props(self):
        node = LeafNode("p",'Hello',  {"src": "image.jpg", "alt": "An image"})
        self.assertEqual(node.to_html(), '<p src="image.jpg" alt="An image">Hello</p>')

    def test_leaf_to_html_no_props(self):
        node = LeafNode("p",'Hello')
        self.assertEqual(node.to_html(), '<p>Hello</p>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, 'Hello')
        self.assertEqual(node.to_html(), 'Hello')


if __name__ == "__main__":
    unittest.main()
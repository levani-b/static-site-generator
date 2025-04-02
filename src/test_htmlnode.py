import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
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



if __name__ == "__main__":
    unittest.main()
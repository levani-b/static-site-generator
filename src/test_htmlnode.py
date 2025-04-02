import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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


    # tests for parent node class
    
    def test_to_html_with_children(self):
        child_node = LeafNode('span', 'child')
        parent_node = ParentNode('p', [child_node])
        self.assertEqual(parent_node.to_html(),"<p><span>child</span></p>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<p><span><b>grandchild</b></span></p>",
        )
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delimeter_italic(self):
        node = TextNode('text with _italic_ word', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("text with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes)
        
    def test_delimeter_bold(self):
        node = TextNode('text with **bold** word', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("text with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes)
        
    def test_delimeter_bold_italic(self):
        node = TextNode('**bold** and _italic_', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes)
    
    def test_delimeter_multi_bold(self):
        node = TextNode('text with two **bold** **word**', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("text with two ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("word", TextType.BOLD),
            ],
            new_nodes)
        
    def test_delimeter_multi_italic(self):
        node = TextNode('text with two _italic_ _word_', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("text with two ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("word", TextType.ITALIC),
            ],
            new_nodes)
    
    def test_delimeter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
            
    def test_non_text_node_unchanged(self):
        node = TextNode('this is already bold', TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertListEqual(
        [
            TextNode("this is already bold", TextType.BOLD)
        ],
        new_nodes)
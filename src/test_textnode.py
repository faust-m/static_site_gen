import unittest
from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    
    def test_not_eq(self):
        node = TextNode("Text Node 1", TextType.CODE)
        node2 = TextNode("Text Node 2", TextType.CODE)
        self.assertNotEqual(node, node2)

    
    def test_repl(self):
        node = TextNode("Text node", TextType.ITALIC)
        self.assertEqual(node.__repr__(), "TextNode(Text node, italic, None)")

    
    def test_htmlnode_text(self):
        node = TextNode("Normal text", TextType.TEXT)
        expected = "LeafNode(None, Normal text, None, None)"
        actual = text_node_to_html_node(node).__repr__()
        self.assertEqual(actual, expected)

    
    def test_htmlnode_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        expected = "LeafNode(b, Bold text, None, None)"
        actual = text_node_to_html_node(node).__repr__()
        self.assertEqual(actual, expected)

    
    def test_htmlnode_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        expected = "LeafNode(i, Italic text, None, None)"
        actual = text_node_to_html_node(node).__repr__()
        self.assertEqual(actual, expected)


    def test_htmlnode_code(self):
        node = TextNode("Code text", TextType.CODE)
        expected = "LeafNode(code, Code text, None, None)"
        actual = text_node_to_html_node(node).__repr__()
        self.assertEqual(actual, expected)


    def test_htmlcode_link(self):
        node = TextNode("Anchor text", TextType.LINK, "https://www.google.com")
        expected = "LeafNode(a, Anchor text, None, {'href': 'https://www.google.com'})"
        actual = text_node_to_html_node(node).__repr__()
        self.assertEqual(actual, expected)


    def test_htmlcode_image(self):
        node = TextNode("Image alt text", TextType.IMAGE, "https://www.image.com/test.png")
        expected = "LeafNode(img, "", None, {'src': 'https://www.image.com/test.png', 'alt': 'Image alt text'})"
        actual = text_node_to_html_node(node).__repr__()
        self.assertEqual(actual, expected)


    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = ["TextNode(This is text with a , text, None)", "TextNode(code block, code, None)", "TextNode( word, text, None)"]
        actual = list(map(lambda n: n.__repr__(), new_nodes))
        self.assertEqual(actual, expected)


    def test_split_nodes_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = ["TextNode(This is text with a , text, None)", "TextNode(bold, bold, None)", "TextNode( word, text, None)"]
        actual = list(map(lambda n: n.__repr__(), new_nodes))
        self.assertEqual(actual, expected)


    def test_split_nodes_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = ["TextNode(This is text with a , text, None)", "TextNode(italic, italic, None)", "TextNode( word, text, None)"]
        actual = list(map(lambda n: n.__repr__(), new_nodes))
        self.assertEqual(actual, expected)


    def test_split_nodes_multiple(self):
        node = TextNode("This is text with an *italic* word and a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter(split_nodes_delimiter([node], "**", TextType.BOLD), "*", TextType.ITALIC)
        expected = ["TextNode(This is text with an , text, None)", "TextNode(italic, italic, None)", "TextNode( word and a , text, None)", "TextNode(bold, bold, None)", "TextNode( word, text, None)"]
        actual = list(map(lambda n: n.__repr__(), new_nodes))
        self.assertEqual(actual, expected)


    def test_split_nodes_except(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "`", TextType.CODE)


    def test_split_nodes_except_first(self):
        node = TextNode("This is text with an *italic word and a **bold** word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "*", TextType.ITALIC)


    def test_split_nodes_except_second(self):
        node = TextNode("This is text with an *italic* word and a **bold* word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "**", TextType.BOLD)



if __name__ == "__main__":
    unittest.main()
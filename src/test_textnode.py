import unittest
from textnode import TextNode, TextType, text_node_to_html_node


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



if __name__ == "__main__":
    unittest.main()
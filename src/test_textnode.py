import unittest
from textnode import TextNode, TextType


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



if __name__ == "__main__":
    unittest.main()
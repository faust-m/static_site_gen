import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_eq_text(self):
        node = TextNode("Text node", TextType.NORMAL)
        node2 = TextNode("Text node", TextType.NORMAL)
        self.assertEqual(node, node2)


    def test_eq_url(self):
        node = TextNode("Text node", TextType.LINK, url="https://www.boot.dev")
        node2 = TextNode("Text node", TextType.LINK, url="https://www.boot.dev")
        self.assertEqual(node, node2)


    def test_eq_url2(self):
        node = TextNode("Text node", TextType.IMAGE, url=None)
        node2 = TextNode("Text node", TextType.IMAGE, url=None)
        self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
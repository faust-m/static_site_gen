import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")


    def test_props_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')
    

    def test_plain_text(self):
        node = LeafNode(None, "This is plain text.")
        self.assertEqual(node.to_html(), "This is plain text.")



if __name__ == "__main__":
    unittest.main()
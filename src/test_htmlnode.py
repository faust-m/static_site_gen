import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_to_html(self):
        node = HTMLNode("a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertRaises(NotImplementedError, node.to_html)

    
    def test_props_to_html(self):
        node = HTMLNode("a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


    def test_repr(self):
        node = HTMLNode("a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), "HTMLNode(a, None, None, {'href': 'https://www.google.com', 'target': '_blank'})")



if __name__ == "__main__":
    unittest.main()
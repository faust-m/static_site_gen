import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_to_html(self):
        node = HTMLNode("a", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertRaises(NotImplementedError(), node.to_html())



if __name__ == "__main__":
    unittest.main()
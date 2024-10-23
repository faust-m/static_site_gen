import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):

    def test_no_children(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError, node.to_html)


    def test_one_child(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
            ]
        )
        expected = "<p><b>Bold text</b></p>"
        self.assertEqual(node.to_html(), expected)

    
    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)


    def test_nested_parents(self):
        node = ParentNode(
            "table",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode("a", "Google", {"href": "https://www.google.com", "target": "_blank"}),
                        LeafNode(None, "Normal text"),
                    ]
                ),
            ]
        )
        expected = '<table><p><b>Bold text</b><a href="https://www.google.com" target="_blank">Google</a>Normal text</p></table>'
        self.assertEqual(node.to_html(), expected)


    def test_nested_leaf_parent(self):
        node = ParentNode(
            "table",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold"),
                        LeafNode("i", "Italic"),
                    ]
                ),
                LeafNode(None, "Normal"),
            ]
        )
        expected = '<table><p><b>Bold</b><i>Italic</i></p>Normal</table>'
        self.assertEqual(node.to_html(), expected)



if __name__ == "__main__":
    unittest.main()
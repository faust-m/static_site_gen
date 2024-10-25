import unittest
from textnode import *


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
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_multiple(self):
        node = TextNode("This is text with an *italic* word and a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    
    def test_split_nodes_beginning(self):
        node = TextNode("**bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_single(self):
        node = TextNode("**bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_double(self):
        node = TextNode("This is text with a **bold** word and another **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and another ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_double_bold(self):
        node = TextNode("**bold****bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode("bold", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_except(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "`", TextType.CODE)


    def test_split_nodes_except_first(self):
        node = TextNode("This is text with an *italic word and a **bold** word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "*", TextType.ITALIC)


    def test_split_nodes_except_second(self):
        node = TextNode("This is text with an *italic* word and a **bold* word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "**", TextType.BOLD)


    def test_extract_md_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpg")]
        actual = extract_markdown_images(text)
        self.assertEqual(actual, expected)


    def test_extract_md_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        actual = extract_markdown_links(text)
        self.assertEqual(actual, expected)


    def test_extract_md_imgs_links(self):
        text = "This text contains a link [to boot dev](https://www.boot.dev) and an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) in it."
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        actual = extract_markdown_images(text)
        self.assertEqual(actual, expected)


    def test_extract_md_links_imgs(self):
        text = "This text contains a link [to boot dev](https://www.boot.dev) and an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) in it."
        expected = [("to boot dev", "https://www.boot.dev")]
        actual = extract_markdown_links(text)
        self.assertEqual(actual, expected)


    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_link_img(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image alt text](https://www.image.com/test.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and an image ![image alt text](https://www.image.com/test.png)", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_link_none(self):
        node = TextNode(
            "This text has no links",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This text has no links", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![image alt text](https://www.image.com/test.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("image alt text", TextType.IMAGE, "https://www.image.com/test.png"),
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_image_link(self):
        node = TextNode(
            "This is text with an image ![image alt text](https://www.image.com/test.png) and a link [link text](https://www.google.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("image alt text", TextType.IMAGE, "https://www.image.com/test.png"),
            TextNode(" and a link [link text](https://www.google.com)", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_image_none(self):
        node = TextNode(
            "This text has no images",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This text has no images", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)


    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(new_nodes, expected)

    
    def test_text_to_textnodes_no_bold(self):
        text = "This is *italic* text with some `code` and a [link](https://www.google.com)"
        new_nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text with some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
        ]
        self.assertEqual(new_nodes, expected)



if __name__ == "__main__":
    unittest.main()
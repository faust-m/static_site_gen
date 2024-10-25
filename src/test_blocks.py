import unittest
from blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode

class TestMarkdownToBlocks(unittest.TestCase):
    
    def test_md_to_blocks(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
* This is a list item
* This is another list item
        
        """
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_blocks_empty(self):
        markdown = ""
        expected = []
        actual = markdown_to_blocks(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_blocks_newlines(self):
        markdown = """# Block1
        
        
        Block2.
        
        
        
        **Bold** text and *italic* text
        
        
        
        """
        expected = [
            "# Block1",
            "Block2.",
            "**Bold** text and *italic* text",
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_h1(self):
        block = "# Heading"
        expected = "heading"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_h2(self):
        block = "## Heading"
        expected = "heading"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_h3(self):
        block = "### Heading"
        expected = "heading"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_h4(self):
        block = "#### Heading"
        expected = "heading"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_h5(self):
        block = "##### Heading"
        expected = "heading"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_h6(self):
        block = "###### Heading"
        expected = "heading"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_code(self):
        block = "```Code block```"
        expected = "code"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_not_code(self):
        block = "```Code block"
        expected = "paragraph"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    
    def test_block_to_block_type_quote(self):
        block = "> Quote_line_1\n> Quote_line_2\n> Quote_line_3"
        expected = "quote"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_not_quote(self):
        block = "> Quote_line_1\n> Quote_line_2\n Quote_line_3"
        expected = "paragraph"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_ul_hyp(self):
        block = "- list_item_1\n- list_item_2\n- list_item_3"
        expected = "unordered_list"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_ul_ast(self):
        block = "* list_item_1\n* list_item_2\n* list_item_3"
        expected = "unordered_list"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_not_ul(self):
        block = "* list_item_1\n- list_item_2\n* list_item_3"
        expected = "paragraph"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_ol(self):
        block = "1. list_item_1\n2. list_item_2\n3. list_item_3"
        expected = "ordered_list"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)


    def test_block_to_block_type_not_ol(self):
        block = "1. list_item_1\n1. list_item_2\n3. list_item_3"
        expected = "paragraph"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    
    def test_block_To_block_type_paragraph(self):
        block = "This is a paragraph"
        expected = "paragraph"
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    
    def test_md_to_html_node_paragraph(self):
        markdown = "This is a paragraph"
        expected = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode(None, "This is a paragraph")])
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_paragraph_formatted(self):
        markdown = "This is a paragraph with *italic* and **bold** text"
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "This is a paragraph with "),
                        LeafNode("i", "italic"),
                        LeafNode(None, " and "),
                        LeafNode("b", "bold"),
                        LeafNode(None, " text"),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_heading(self):
        markdown = "### This is a heading"
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "h3",
                    [
                        LeafNode(None, "This is a heading"),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_heading_formatted(self):
        markdown = "## Heading with **bold** and *italic*"
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "h2",
                    [
                        LeafNode(None, "Heading with "),
                        LeafNode("b", "bold"),
                        LeafNode(None, " and "),
                        LeafNode("i", "italic"),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_code(self):
        markdown = "```print('test')```"
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "pre",
                    [
                        LeafNode("code", "print('test')"),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)

    
    def test_md_to_html_node_quote(self):
        markdown = ">This is a quote."
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "blockquote",
                    [
                        LeafNode(None, "This is a quote."),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_quote_lines(self):
        markdown = ">This is line one.\n>This is line two."
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "blockquote",
                    [
                        LeafNode(None, "This is line one.\nThis is line two."),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_quote_formatted(self):
        markdown = ">This is a quote with a **bold** word."
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "blockquote",
                    [
                        LeafNode(None, "This is a quote with a "),
                        LeafNode("b", "bold"),
                        LeafNode(None, " word."),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_ol(self):
        markdown = "1. list_item_1\n2. list_item_2\n3. list_item_3"
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "ol",
                    [
                        ParentNode("li", [LeafNode(None, "list_item_1")]),
                        ParentNode("li", [LeafNode(None, "list_item_2")]),
                        ParentNode("li", [LeafNode(None, "list_item_3")]),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_ol_formatted(self):
        markdown = "1. list_item_1\n2. **list_item_2**\n3. *list_item_3*"
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "ol",
                    [
                        ParentNode("li", [LeafNode(None, "list_item_1")]),
                        ParentNode("li", [LeafNode("b", "list_item_2")]),
                        ParentNode("li", [LeafNode("i", "list_item_3")])
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_ul(self):
        markdown = "* list_item_1\n* list_item_2\n* list_item_3"
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "ul",
                    [
                        ParentNode("li", [LeafNode(None, "list_item_1")]),
                        ParentNode("li", [LeafNode(None, "list_item_2")]),
                        ParentNode("li", [LeafNode(None, "list_item_3")]),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)


    def test_md_to_html_node_ul_formatted(self):
        markdown = "* *list_item_1*\n* list_item_2\n* **list_item_3**"
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "ul",
                    [
                        ParentNode("li", [LeafNode("i", "list_item_1")]),
                        ParentNode("li", [LeafNode(None, "list_item_2")]),
                        ParentNode("li", [LeafNode("b", "list_item_3")]),
                    ]
                )
            ]
        )
        actual = markdown_to_html_node(markdown)
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()
import functools
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import *

def markdown_to_blocks(markdown):
    blocks = markdown.splitlines(keepends=True)
    blocks = [block.strip() for block in blocks]
    markdown = functools.reduce(lambda acc, line: acc + f"{line}\n", blocks, "")
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks]
    blocks = list(filter(lambda item: item != "" and item != "\n", blocks))
    return blocks



def block_to_block_type(block):
    if block.startswith(
        (
            "# ",
            "## ",
            "### ",
            "#### ",
            "##### ",
            "###### ",
        )
    ):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        lines = block.splitlines()
        filtered_lines = list(filter(lambda line: line.startswith(">"), lines))
        if lines == filtered_lines:
            return "quote"
    elif block.startswith("* "):
        lines = block.splitlines()
        filtered_lines = list(filter(lambda line: line.startswith("* "), lines))
        if lines == filtered_lines:
            return "unordered_list"
    elif block.startswith("- "):
        lines = block.splitlines()
        filtered_lines = list(filter(lambda line: line.startswith("- "), lines))
        if lines == filtered_lines:
            return "unordered_list"
    elif block.startswith("1. "):
        lines = block.splitlines()
        i = 0
        while i < len(lines):
            if not lines[i].startswith(f"{i + 1}. "):
                break
            i += 1
        if i == len(lines):
            return "ordered_list"
    return "paragraph"
    


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes


def markdown_to_html_node(markdown):
    children_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        match block_to_block_type(block):
            case "paragraph":
                children_nodes.append(ParentNode("p", text_to_children(block)))
            case "heading":
                h_value = len(block) - len(block.lstrip("#"))
                children_nodes.append(ParentNode(f"h{h_value}", text_to_children(block.lstrip("# "))))
            case "code":
                children_nodes.append(ParentNode("pre", text_to_children(block.strip())))
            case "quote":
                lines = block.splitlines(keepends=True)
                lines = [line.removeprefix(">") for line in lines]
                block = functools.reduce(lambda acc, line: acc + line, lines, "")
                children_nodes.append(ParentNode("blockquote", text_to_children(block.strip())))
            case "ordered_list":
                items = block.splitlines()
                items = [item.lstrip("1234567890. ") for item in items]
                children = [ParentNode("li", text_to_children(item)) for item in items]
                children_nodes.append(ParentNode("ol", children))
            case "unordered_list":
                items = block.splitlines()
                items = [item.lstrip("*-").lstrip() for item in items]
                children = [ParentNode("li", text_to_children(item)) for item in items]
                children_nodes.append(ParentNode("ul", children))
    return ParentNode("div", children_nodes)
import re
from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid TextType")
        


def extract_markdown_images(text):
    image_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_list



def extract_markdown_links(text):
    link_list = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return link_list
        


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        node_texts = node.text.split(delimiter)
        if len(node_texts) % 2 == 0:
            raise Exception("Invalid Markdown text")
        for i in range(len(node_texts)):
            if node_texts[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(node_texts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(node_texts[i], text_type))
    return new_nodes



def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        split_nodes = re.split(r"(!\[.*?\]\(.*?\))", node.text)
        for split_node in split_nodes:
            if split_node == "":
                continue
            image_data = extract_markdown_images(split_node)
            if len(image_data) == 0:
                new_nodes.append(TextNode(split_node, TextType.TEXT))
            else:
                new_nodes.append(TextNode(image_data[0][0], TextType.IMAGE, image_data[0][1]))
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        split_nodes = re.split(r"(?<!!)(\[.*?\]\(.*?\))", node.text)
        for split_node in split_nodes:
            if split_node == "":
                continue
            link_data = extract_markdown_links(split_node)
            if len(link_data) == 0:
                new_nodes.append(TextNode(split_node, TextType.TEXT))
            else:
                new_nodes.append(TextNode(link_data[0][0], TextType.LINK, link_data[0][1]))
    return new_nodes



def text_to_textnodes(text):
    node = TextType(
        text,
        TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter([new_nodes], "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter([new_nodes], "`", TextType.CODE)
    new_nodes = split_nodes_image([new_nodes])
    new_nodes = split_nodes_link([new_nodes])
    return new_nodes



class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    
    def __eq__(self, other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )
    

    def __repr__(self):
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"
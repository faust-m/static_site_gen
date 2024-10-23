from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is needed for a ParentNode")
        if self.children == None:
            raise ValueError("Children are required for a ParentNode")
        return f"<{self.tag}{self.props_to_html()}>{self.__html_str_conversion(self.children)}</{self.tag}>"
    

    def __html_str_conversion(self, nodes):
        if len(nodes) == 1:
            return nodes[0].to_html()
        return nodes[0].to_html() + self.__html_str_conversion(nodes[1::])

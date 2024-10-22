import functools


class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError("HTMLNode() does not implement this.")
    

    def props_to_html(self):
        return functools.reduce(
            lambda result, item: result + item[0] + "=" + item[1] + " ",
            self.props.items(),
            " "
        )
    
    
    def __repr__(self):
        return f"{__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"
import functools


class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError("HTMLNode() does not implement to_html()")
    

    def props_to_html(self):
        if self.props == None:
            return ""
        return functools.reduce(
            lambda result, item: result + item[0] + "=\"" + item[1] + "\" ",
            self.props.items(),
            " "
        ).rstrip(" ")
    
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})'
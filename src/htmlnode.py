#!/usr/bin/env python3


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        props_string = ""
        if self.props is not None:
            for k, v in self.props.items():
                props_string += " " + k + '="' + v + '"'
        return props_string

    def __repr__(self) -> str:
        props = "None"
        if self.props is not None:
            props = self.props_to_html()
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return super().__repr__()


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str | None:
        if self.tag == None:
            raise ValueError("Tag is needed!")
        html_string = ""
        if self.children != None:
            html_string += f"<{self.tag}>"
            for child in self.children:
                html_string += child.to_html()
            html_string += f"</{self.tag}>"
        else:
            raise ValueError("No Children!")

        return html_string

    def __repr__(self) -> str:
        return super().__repr__()

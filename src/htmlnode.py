class HTMLNode():
    def __init__(self,tag = None,value = None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError('to_html not implemented')
    
    def props_to_html(self):
        prop_html = ""

        if self.props is None:
            return ''

        for key,val in self.props.items():
            prop_html += f' {key}="{val}"'
        return prop_html
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
from src.textnode import TextNode, TextType
from src.splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    # Start with a single TextNode using the proper TextType enum
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Final check: ensure all .text_type are proper TextType enums
    for node in nodes:
        if not isinstance(node.text_type, TextType):
            raise TypeError(f"Invalid text_type: {node.text_type}, expected TextType enum")
    return nodes

from markdown_blocks import markdown_to_blocks
from block_parser import block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode, text_node_to_html_node
from text_parser import text_to_textnodes
from textnode import TextType

def text_to_children(text):
    # This function assumes text_to_textnodes returns TextNode objects
    # with .text_type correctly set to a TextType enum
    parsed_nodes = text_to_textnodes(text)
    for node in parsed_nodes:
        if not isinstance(node.text_type, TextType):
            raise TypeError(f"Invalid text_type: {node.text_type}, expected TextType enum")
    return [text_node_to_html_node(node) for node in parsed_nodes]

def paragraph_block_to_html(block):
    children = text_to_children(block)
    return ParentNode("p", children)

def heading_block_to_html(block):
    level = len(block.split(" ")[0])
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_block_to_html(block):
    lines = block.split("\n")
    content = "\n".join(lines[1:-1]) + "\n"
    code_node = LeafNode("code", content)
    return ParentNode("pre", [code_node])

def quote_block_to_html(block):
    lines = [line.lstrip("> ").strip() for line in block.split("\n")]
    joined = " ".join(lines)
    children = text_to_children(joined)
    return ParentNode("blockquote", children)

def unordered_list_block_to_html(block):
    items = [line.lstrip("- ").strip() for line in block.split("\n")]
    li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
    return ParentNode("ul", li_nodes)

def ordered_list_block_to_html(block):
    items = [line.split(". ", 1)[1].strip() for line in block.split("\n")]
    li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
    return ParentNode("ol", li_nodes)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block_nodes.append(paragraph_block_to_html(block))
        elif block_type == BlockType.HEADING:
            block_nodes.append(heading_block_to_html(block))
        elif block_type == BlockType.CODE:
            block_nodes.append(code_block_to_html(block))
        elif block_type == BlockType.QUOTE:
            block_nodes.append(quote_block_to_html(block))
        elif block_type == BlockType.UNORDERED_LIST:
            block_nodes.append(unordered_list_block_to_html(block))
        elif block_type == BlockType.ORDERED_LIST:
            block_nodes.append(ordered_list_block_to_html(block))
        else:
            raise Exception(f"Unknown BlockType: {block_type}")

    return ParentNode("div", block_nodes)

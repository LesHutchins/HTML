import unittest

from textnode import (
    TextNode,
    TextType,
    text_to_textnodes,
    split_nodes_delimiter,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("A link", TextType.LINK, "https://example.com")
        node2 = TextNode("A link", TextType.LINK, "https://different.com")
        self.assertNotEqual(node1, node2)

    def test_text_to_textnodes(self):
        result = text_to_textnodes("Hello, markdown!")
        expected = [TextNode("Hello, markdown!", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter(self):
        nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        split = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(split, expected)


if __name__ == "__main__":
    unittest.main()

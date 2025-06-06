import unittest

from src.textnode import TextNode, TextType
from src.splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link


class TestSplitter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_image_single(self):
        node = TextNode("Here is an ![example](https://example.com/img.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("example", TextType.IMAGE, "https://example.com/img.png"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_link_single(self):
        node = TextNode("Visit [Google](https://google.com) now", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" now", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_image_no_match(self):
        node = TextNode("No image here", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [TextNode("No image here", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)

    def test_split_link_no_match(self):
        node = TextNode("No link here", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [TextNode("No link here", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()

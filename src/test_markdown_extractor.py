import unittest

from markdown_extractor import extract_markdown_images, extract_markdown_links


class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a [link](https://boot.dev) in the text"
        )
        self.assertListEqual(
            [("link", "https://boot.dev")],
            matches,
        )

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "Look at ![one](url1.png) and ![two](url2.png)"
        )
        self.assertListEqual(
            [("one", "url1.png"), ("two", "url2.png")],
            matches,
        )

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "See [Boot.dev](https://boot.dev) and [Google](https://google.com)"
        )
        self.assertListEqual(
            [("Boot.dev", "https://boot.dev"), ("Google", "https://google.com")],
            matches,
        )

    def test_ignore_non_markdown(self):
        matches = extract_markdown_links("This is not a [markdown link")
        self.assertListEqual([], matches)

        matches = extract_markdown_images("This is not a ![markdown image")
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()

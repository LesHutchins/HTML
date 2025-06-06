import unittest

from src.markdown_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_trailing_newlines(self):
        md = """
First block

Second block


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["First block", "Second block"],
        )

    def test_empty_input(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = "Single block without any double newlines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Single block without any double newlines"])

    def test_multiple_paragraphs_and_list(self):
        md = """
Paragraph one

Paragraph two

- List item one
- List item two
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Paragraph one",
                "Paragraph two",
                "- List item one\n- List item two",
            ],
        )


if __name__ == "__main__":
    unittest.main()

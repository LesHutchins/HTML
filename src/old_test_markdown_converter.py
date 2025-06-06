import unittest
from src.markdown_converter import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p tag

Another _italic_ line here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag</p><p>Another <i>italic</i> line here</p></div>",
        )

    def test_codeblock(self):
        md = """```
code line 1
code line 2
```"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>code line 1\ncode line 2\n</code></pre></div>",
        )

    def test_heading_h1(self):
        md = "# Heading One"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading One</h1></div>",
        )

    def test_heading_h3(self):
        md = "### Heading Three"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Heading Three</h3></div>",
        )

    def test_unordered_list(self):
        md = "- Item A\n- Item B\n- Item C"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item A</li><li>Item B</li><li>Item C</li></ul></div>",
        )

    def test_ordered_list(self):
        md = "1. First\n2. Second\n3. Third"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>",
        )

    def test_quote_block(self):
        md = "> This is a quote\n> spanning two lines"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote spanning two lines</blockquote></div>",
        )

    def test_mixed_inline(self):
        md = "Text with **bold**, _italic_, and `code`."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Text with <b>bold</b>, <i>italic</i>, and <code>code</code>.</p></div>",
        )

    def test_empty_input(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div></div>",
        )

    def test_multiple_blocks(self):
        md = (
            "# Header\n\n"
            "Paragraph here\n\n"
            "- List item 1\n"
            "- List item 2\n\n"
            "```\n"
            "code block content\n"
            "```"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Header</h1><p>Paragraph here</p><ul><li>List item 1</li><li>List item 2</li></ul><pre><code>code block content\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()

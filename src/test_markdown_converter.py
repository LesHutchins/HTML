import unittest
from src.markdown_converter import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = "This is **bolded** paragraph text in a p tag\n\nAnother _italic_ line here"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag</p><p>Another <i>italic</i> line here</p></div>",
        )

    # Keep other tests as-is (assuming they were working or will be re-checked later)

if __name__ == "__main__":
    unittest.main()
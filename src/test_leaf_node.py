import unittest
from leaf_node import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just some text.")
        self.assertEqual(node.to_html(), "Just some text.")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "highlighted")
        self.assertEqual(node.to_html(), "<span>highlighted</span>")

    def test_leaf_missing_value_raises(self):
        with self.assertRaises(ValueError):
            LeafNode("b", None)

if __name__ == "__main__":
    unittest.main()

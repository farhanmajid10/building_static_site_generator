import unittest
from utils import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote,
)

class TestBlockToBlockType(unittest.TestCase):
    def test_code(self):
        text = "```apvdser jfesrg efsaef. \nfesjgag\nrewgwags```"
        result = block_to_block_type(text)
        self.assertEqual(result, "code")
    
    def test_quote(self):
        text = "> apvdser jfesrg efsaef.## \n> fesjgag\n> rewgwags```"
        result = block_to_block_type(text)
        self.assertEqual(result, "quote")
    
    def test_quotes(self):
        text = "> apvdser jfesrg efsaef.## \n> fesjgag\n> rewgwags```"
        result = block_to_block_type(text)
        self.assertEqual(result, "quote")

    def test_heading1(self):
        text = "# sfjkdsa m , m\n djiowah ```"
        result = block_to_block_type(text)
        self.assertEqual(result, "heading")

    def test_heading2(self):
        text = "## sfjkdsa m , m\n djiowah ```"
        result = block_to_block_type(text)
        self.assertEqual(result, "heading")
    
    def test_heading3(self):
        text = "### sfjkdsa m , m\n djiowah ```"
        result = block_to_block_type(text)
        self.assertEqual(result, "heading")
    
    def test_heading6(self):
        text = "###### sfjkdsa m , m\n djiowah ```"
        result = block_to_block_type(text)
        self.assertEqual(result, "heading")
    
    def test_hashes7(self):
        text = "####### sfjkdsa m , m\n djiowah ```"
        result = block_to_block_type(text)
        self.assertEqual(result, "paragraph")
    
    def test_unordered_list(self):
        text = "- ###### sfjkdsa m , m\n-   djiowah ```"
        result = block_to_block_type(text)
        self.assertEqual(result, "unordered_list")

    def test_ordered_list(self):
        text = "1.  ###### sfjkdsa m , m\n2.   dji\n3. owah ```"
        result = block_to_block_type(text)
        self.assertEqual(result, "ordered_list")
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

        

if __name__ == "__main__":
    unittest.main()
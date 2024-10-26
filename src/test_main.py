import unittest
from main import extract_title


class TestMain(unittest.TestCase):

    def test_extract_title(self):
        expected = "Test"
        actual = extract_title("# Test")
        self.assertEqual(actual, expected)


    def test_extract_title_empty(self):
        self.assertRaises(Exception, extract_title, "")


    def test_extract_title_multiple(self):
        self.assertRaises(Exception, extract_title, "## Title")


    def test_extract_title(self):
        expected = "Test"
        actual = extract_title("#Test")
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()
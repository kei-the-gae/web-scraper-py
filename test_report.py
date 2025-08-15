import unittest
from report import sort_pages


class TestReport(unittest.TestCase):
    def test_sort_pages(self):
        input_dict = {"url1": 5, "url2": 1, "url3": 3, "url4": 10, "url5": 7}
        actual = sort_pages(input_dict)
        expected = [("url4", 10), ("url5", 7), ("url1", 5), ("url3", 3), ("url2", 1)]
        self.assertEqual(actual, expected)

    def test_sort_pages_null_case(self):
        input_dict = {}
        actual = sort_pages(input_dict)
        expected = []
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

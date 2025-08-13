import unittest
from crawl import normalize_url, get_urls_from_html


class TestCrawl(unittest.TestCase):
    def test_normalize_url_protocol(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_slash(self):
        input_url = "https://blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_capitals(self):
        input_url = "https://BLOG.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_http(self):
        input_url = "http://BLOG.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_absolute(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="https://blog.boot.dev"><span>Boot.dev></span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_relative(self):
        input_url = "https://blog.boot.dev"
        input_body = (
            '<html><body><a href="/path/one"><span>Boot.dev></span></a></body></html>'
        )
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/path/one"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_both(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="/path/one"><span>Boot.dev></span></a><a href="https://other.com/path/one"><span>Boot.dev></span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/path/one", "https://other.com/path/one"]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

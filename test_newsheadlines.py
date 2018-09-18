import unittest
from unittest.mock import patch
from newsheadlines import cli


class NewsTest(unittest.TestCase):

    @patch("builtins.input", return_value="1")
    def test_cli_function(self, input):
        url = 'https://newsapi.org/v2/top-headlines?sources=fox-news&apiKey='+ +'&pageSize=10'
        expected_output = (requests.get(url).json()['articles'])
        self.assertEqual(cli(), expected_output)
        

if __name__ == '__main__':
    unittest.main()

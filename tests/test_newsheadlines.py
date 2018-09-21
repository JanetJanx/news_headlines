import unittest

import requests

from app.newsheadlines import NewsHeadlines

class TestNews(unittest.TestCase):
    def setUp(self):
        self.news = NewsHeadlines()

    def test_api_key_collection(self):
        self.assertEqual(self.news.get_key(), '9b40cf73093e47e586cd61132f1d56fe')
    
    def test_cli_function(self):
        api_key = self.news.get_key()
        url = 'https://newsapi.org/v2/top-headlines?sources=fox-news&apiKey='+api_key+'&pageSize=10'
        news_sources = requests.get(url).json()['articles']
        test_count = 0
        for article in news_sources:
            test_count = test_count + 1
            title = article['title']
            description = article['description']
            article_url = article['url']
            test_headlines = "..... {} .....\n Title: {}\n Description: {} \n Link: {}\n".format(test_count, title, description, article_url)
        self.assertEqual(self.news.cli('1'), test_headlines)

if __name__ == "__main__":
    unittest.main() 
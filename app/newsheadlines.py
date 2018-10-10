import click
import os
import click
import requests

class NewsHeadlines:
    def news_source_menu(self):
        menu = ('Select your favorate source of News'+ '\n' + '1. FOX-News' + '\n' + '2. CNN' + '\n' +
            '3. Al- Jazeera - english'+ '\n' + '4. BBC-Sport'+ '\n' + '-' * 100)
        click.echo(click.style(menu, fg='blue'))
        return menu


    def news_board(self):
        board = ('\n'+ '*' * 100 + '*' + ' ' * 98 +' ' * 98 + '\n' +' ' * 30 +
                'News HeadLines ' + ' ' * 32 + '*' + '*' + '\n'+' ' * 12 + 'The latest and Live breaking news headlines '
                + ' ' * 26 + '*' + '*' + ' ' * 98 + '*' + '*' + ' ' * 98 + '\n'+'*' + '*' * 100 + '\n')
        click.echo(click.style(board, fg='blue'))
        return board

    def get_key(self):
        return os.environ.get('API_KEY')

    def fetch_newsheadlines(self):
        sources = {'1':'fox-news', '2':'cnn','3':'al-jazeera-english','4':'bbc-sport'}
        api_key = NewsHeadlines().get_key()
        for news_source in sources:
            if news_source == source_number:
                url='https://newsapi.org/v2/top-headlines?sources='+sources[news_source]+'&apiKey='+api_key+'&pageSize=10'
                click.echo(click.style('Please wait as we retrive from news headlines from '+ sources[news_source], fg='magenta'))
                news_sources = requests.get(url).json()['articles']
                return news_sources


class NewsDisplay:
    def cli(self):
        news_headlines = NewsHeadlines().fetch_newsheadlines()
        count = 0
        for article in news_headlines:
            count = count + 1
            title = article['title']
            description = article['description']
            article_url = article['url']

            headlines = "..... {} .....\n Title: {}\n Description: {} \n Link: {}\n".format(count, title, description, article_url)
            click.echo(click.style(headlines, fg='green'))
        return headlines



display = NewsHeadlines()
display.news_board()
display.news_source_menu()
source_number = input('> Enter the number of your Favorate Source of News here: ')
news_display = NewsDisplay()
news_display.cli()
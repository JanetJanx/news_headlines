import click
import os
import click
import requests

class NewsHeadlines:
    def news_source_menu(self):
        menu = ('Select your favorate source of News'+ '\n' + '1. FOX-News' + '\n' + '2. CNN' + '\n' + 
            '3. Al- Jazeera - english'+ '\n' + '4. BBC-Sport'+ '\n' + '-' * 100)
        return click.echo(click.style(menu, fg='blue'))
        

    def news_board(self):
        board = ('\n'+ '*' * 100 + '*' + ' ' * 98 +' ' * 98 + '\n' +' ' * 30 + 
                'News HeadLines ' + ' ' * 32 + '*' + '*' + '\n'+' ' * 12 + 'The latest and Live breaking news headlines ' 
                + ' ' * 26 + '*' + '*' + ' ' * 98 + '*' + '*' + ' ' * 98 + '\n'+'*' + '*' * 100 + '\n')
        return click.echo(click.style(board, fg='blue'))
    
    def get_key(self):
        if 'API_KEY' not in os.environ:
            raise ValueError("Your Key is invalid! Access Denied")
        return os.environ.get('API_KEY')


class NewsDisplay:
    def cli(self, source_number):
        sources = {'1':'fox-news', '2':'cnn','3':'al-jazeera-english','4':'bbc-sport'}
        api_key = NewsHeadlines().get_key()
        for news_source in sources:

            if news_source == source_number :
                url='https://newsapi.org/v2/top-headlines?sources='+sources[news_source]+'&apiKey='+api_key+'&pageSize=10'
                click.echo(click.style('Please wait as we retrive from news headlines from FOX-news', fg='magenta'))
                news_request = requests.get(url)
                news_sources = news_request.json()['articles']
                count = 0
                for article in news_sources:
                    count = count + 1
                    title = article['title']
                    description = article['description']
                    article_url = article['url']

                    headlines = "..... {} .....\n Title: {}\n Description: {} \n Link: {}\n".format(count, title, description, article_url)
                    click.echo(click.style(headlines, fg='green'))
                return headlines


if __name__ == "__main__":
    display = NewsHeadlines()
    display.news_board()
    display.news_source_menu()
    source_number = input('> Enter the number of your Favorate Source of News here: ')
    news_display = NewsDisplay()
    news_display.cli(source_number)
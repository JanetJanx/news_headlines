import click
import requests


def news_source_menu():
    menu = ('Select your favorate source of News'+ '\n' + '1. FOX-News' + '\n' + '2. CNN' + '\n' + 
           '3. Al- Jazeera - english'+ '\n' + '4. BBC-Sport'+ '\n' + '-' * 100)
    click.echo(click.style(menu, fg='blue'))
    

def news_board():
    board = ('\n'+ '*' * 100 + '*' + ' ' * 98 + '*' + '*' + ' ' * 98 + '*' + '*' + ' ' * 30 + 
            'News HeadLines ' + ' ' * 32 + '*' + '*' + ' ' * 54 + 'The latest and Live breaking news headlines ' 
            + ' ' * 12 + '*' + '*' + ' ' * 98 + '*' + '*' + ' ' * 98 + '*' + '*' * 100 + '\n')
    click.echo(click.style(board, fg='blue'))
    

@click.command()
def cli():

    news_board()
    news_source_menu()
    source_number = input('> Enter the number of your Favorate Source of News here: ')
    api_key = '9b40cf73093e47e586cd61132f1d56fe'
    sources = {'1':'fox-news', '2':'cnn','3':'al-jazeera-english','4':'bbc-sport'}

    for news_source in sources:

        if news_source == source_number :
            url='https://newsapi.org/v2/top-headlines?sources='+sources[news_source]+'&apiKey='+api_key+'&pageSize=10'
            click.echo(click.style('Please wait as we retrive from news headlines from FOX-news', fg='magenta'))
            news_request = requests.get(url)
            news_sources = news_request.json()['articles']
            count = 0
            for article in news_sources:
                count = count + 1
                headlines = ('......................'+ str(count) +'............................' + '\n'+
                            'Title: ' + article['title'] + '\n'+'Description: ' + str(article['description']) +'\n'+
                            'Link: ' + article['url'] + '\n')
                click.echo(click.style(headlines, fg='green'))
            return headlines
cli()
import click
import requests
#not in range expection error
class NotInRangeError(Exception):
    pass

def news_source_menu():
    click.echo(click.style('Select your favorate source of News', fg='blue'))
    click.echo(click.style('1. FOX-News', fg='blue'))
    click.echo(click.style('2. CNN', fg='blue'))
    click.echo(click.style('3. Al- Jazeera - english', fg='blue'))
    click.echo(click.style('4. BBC-Sport', fg='blue'))
    click.echo(click.style('-' * 100, fg='blue'))


def news_board():
    click.echo('\n')
    click.echo(click.style('*' * 100, fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 32 + 'News HeadLines ' + ' ' * 32 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 22 + 'The latest and Live breaking news headlines ' + ' ' * 12 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' * 100, fg='blue'))
    click.echo('\n')


@click.command()
def cli():

    news_board()
    news_source_menu()
    news_source_number = input('> Enter the number of your Favorate Source of News here: ')

    if news_source_number not in ("1", "2", "3", "4"):
        raise NotInRangeError("Please select numbers between 0 and 4")
   
    if news_source_number == "1":
        url="https://newsapi.org/v2/top-headlines?sources=fox-news&apiKey=9b40cf73093e47e586cd61132f1d56fe&pageSize=10"
        
    if news_source_number == "2":
        url="https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=9b40cf73093e47e586cd61132f1d56fe&pageSize=10"
        
    if news_source_number == "3":
        url="https://newsapi.org/v2/top-headlines?sources=al-jazeera-english&apiKey=9b40cf73093e47e586cd61132f1d56fe&pageSize=10"
        
    if news_source_number == "4":
        url="https://newsapi.org/v2/top-headlines?sources=bbc-sport&apiKey=9b40cf73093e47e586cd61132f1d56fe&pageSize=10"
        
    news_request = requests.get(url)
    news_sources = news_request.json()
    article_list = news_sources['articles']
    count = 0    
    for article in article_list:
        count = count + 1
        click.echo(click.style('......................'+ str(count) +'............................', fg='green'))
        click.echo(click.style('Title: ' + article['title'], fg='green'))
        click.echo(click.style('Description: ' + str(article['description']), fg='magenta'))
        click.echo(click.style('Link: ' + article['url'], fg='blue'))
        click.echo('\n')
   
cli()
import click
import requests

def greeting():
    print("Select your favorate source of News")
    user_name = input('> What\'s your it here?: ')
    print('-' * 100)


def draw_header():
    click.echo('\n')
    click.echo(click.style('*' * 100, fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 32 + 'News HeadLines ' + ' ' * 32 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 32 + 'The latest and Live breaking news headlines ' + ' ' * 12 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' * 100, fg='blue'))
    click.echo('\n')


@click.command()
def cli():

    draw_header()
    greeting()
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=9b40cf73093e47e586cd61132f1d56fe&pageSize=10"
    news_request = requests.get(url)
    main_dict = news_request.json()
    article_list = main_dict['articles']
    count = 0
    for article in article_list:
        count = count + 1
        click.echo(click.style('TITLE: ' + article['title'], fg='green'))
        click.echo('\n')
        click.echo(click.style('description: ' + str(article['description']), fg='yellow'))
        click.echo('\n')
        click.echo(click.style('BY: ' + article['url'], fg='blue'))
        click.echo(click.style('......................'+ str(count) +'............................', fg='green'))
        click.echo('\n')
        #click.echo('o', 'red')


cli()
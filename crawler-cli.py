import click

from robotstxtpy.crawler import Crawler
from robotstxtpy.utils import validate_url


@click.command()
@click.option('--agent', prompt='who is the user-agent',
              help='user agent')
def add_user_agent(agent):
    if agent.isspace():
        click.echo('No user agent added. Please enter a user_agent')
        add_user_agent()
    elif agent == 'exit':
        return
    else:
        click.echo('User agent is %s' % agent)
        url_input()


@click.command()
@click.option('--ans', prompt='more user-agents to add',
              help="'y' to add more user-agents 'n' to produce the robots.txt")
def more_user_agent(ans):
    if ans == 'y':
        click.echo('y')
    elif ans == 'n':
        click.echo('n')
    else:
        click.echo('that is not a valid answer')
        more_user_agent()


@click.command()
@click.option('--url', prompt='Enter URL to generate robots.txt',
              help='Enter URL to be crawled (must be base path to website)')
def url_input(URL):
    if not URL:
        click.echo('Enter a URL!')
        url_input()
    elif not validate_url(URL):
        click.echo('Invalid URL')
        url_input()

    crawler = Crawler(URL)
    urls = crawler.get_endpoints_from_url()
    click.echo(urls)

# asks user for user agent
# asks user for URL
# generate robot.txt


if __name__ == '__main__':
    add_user_agent()

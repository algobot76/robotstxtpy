import click

from robotstxtpy import RobotsTxt
from robotstxtpy.crawler import Crawler
from robotstxtpy.utils import filter_out_path_from_url

user_agent_list = []
robottxt = RobotsTxt()


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
        user_agent_list.append(agent)
        more_user_agent()


@click.command()
@click.option('--ans', prompt='Add more user-agents?(y/n)',
              help="'y' to add more user-agents 'n' to produce the robots.txt")
def more_user_agent(ans):
    if ans == 'y':
        click.echo('y')
        add_user_agent()
    elif ans == 'n':
        click.echo('n')
        url_input()
    else:
        click.echo('that is not a valid answer')


@click.command()
@click.option('--url', prompt='Enter URL to generate robots.txt',
              help='Enter URL to be crawled (must be base path to website)')
def url_input(url):
    if url.isspace():
        click.echo('Enter a URL!')
        url_input()
    else:
        crawler = Crawler(url)
        urls = crawler.get_endpoints_from_url()
        post_process(urls, user_agent_list)
        path_input()


@click.command()
@click.option('--path',
              prompt='Enter path to generate file(default current dir)',
              help='Enter path to be crawled')
def path_input(path):
    if path.isspace():
        robottxt.generate('.')
    else:
        robottxt.generate(path)

# Preprocess urls gathered by crawler
# returns a processed set of URLs
def post_process(urls, user_agent_list):
    for agent in user_agent_list:
        robottxt.add_user_agent(agent)
        for url in urls:
            endpoint = filter_out_path_from_url(url)
            if len(endpoint) != 0:
                robottxt.add_endpoint(agent, 'Disallow', endpoint)

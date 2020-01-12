import click


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
        add_allowed_url()


@click.command()
@click.option('--allowed_url', prompt='Enter "Allow" endpoints or "n" to skip',
              help='"Allow" endpoints or "n" to skip')
def add_allowed_url(allowed_url):
    if allowed_url == 'exit':
        return
    elif allowed_url == 'n':
        add_disallowed_url()
    elif allowed_url[:1] == '/':
        click.echo('endpoint added : %s' % allowed_url)
        add_allowed_url()
    else:
        click.echo('endpoint needs to start with /')
        add_allowed_url()


@click.command()
@click.option('--disallowed_url',
              prompt='Enter "Disallow" endpoints or "n" to skip',
              help='"Disallow" endpoint or "n" to skip')
def add_disallowed_url(disallowed_url):
    if disallowed_url == 'exit':
        return
    elif disallowed_url == 'n':
        more_user_agent()
    elif disallowed_url[:1] == '/':
        click.echo('Disallow endpoint added : %s' % disallowed_url)
        add_disallowed_url()
    else:
        click.echo('endpoint needs to start with /')
        add_disallowed_url()


@click.command()
@click.option('--ans', prompt="'y' to add more user-agents "
                              "'n' to produce the robots.txt",
              help="'y' to add more user-agents 'n' to produce the robots.txt")
def more_user_agent(ans):
    if ans == 'y':
        click.echo('y')
        add_user_agent()
    elif ans == 'n':
        click.echo('n')
    elif ans == 'exit':
        click.echo('exit')
    else:
        click.echo('that is not a valid answer')
        more_user_agent()

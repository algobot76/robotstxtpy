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
        allowed_url()

@click.command()
@click.option('--allow_url', prompt='Enter "Allow" endpoints or "n" to skip',
               help='"Allow" endpoints or "n" to skip')
def allowed_url(allow_url):
    
    if allow_url == 'exit':
        return
    elif allow_url == 'n':
        disallowed_url()
    elif allow_url[:1] == '/':
        click.echo('endpoint added : %s' %  allow_url)
        allowed_url()
    else :
        click.echo('endpoint needs to start with /')
        allowed_url()

@click.command()
@click.option('--disallow', prompt='Enter "Disallow" endpoints or "n" to skip',
                help='"Disalllow" endpoint or "n" to skip')
def disallowed_url(disallow):
    if disallow == 'exit':
        return
    elif disallow == 'n':
        more_user_agent()
    elif disallow[:1] == '/':
        click.echo('Disallow endpoint added : %s' %  disallow)
        disallowed_url()
    else :
        click.echo('endpoint needs to start with /')
        disallowed_url()


@click.command()
@click.option('--ans', prompt='more user-agents to add',
                help="'y' to add more user-agents 'n' to produce the robots.txt")
def more_user_agent(ans):
    if ans == 'y':
        click.echo('y')
    elif ans == 'n':
        click.echo('n')
    else : 
        click.echo('that is not a valid answer')
        more_user_agent()


#ask for user agent
#ask permision 
#ask for end point 

if __name__ == '__main__':
    add_user_agent()
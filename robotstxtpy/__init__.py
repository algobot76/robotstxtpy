from itertools import chain

from robotstxtpy.exceptions import RobotsTxtException


class RobotsTxt:

    def __init__(self):
        self.content = dict()

    def add_user_agent(self, user_agent):
        result = self.content.get(user_agent, None)
        if result is None:
            self.content[user_agent] = []

    def add_endpoint(self, user_agent, permission, endpoint):
        if user_agent not in self.content:
            raise RobotsTxtException()
        self.content[user_agent].append((permission, endpoint))

    def user_agents(self):
        return list(self.content.keys())

    def rules(self, user_agent=None):
        if user_agent is None:
            return list(chain.from_iterable(self.content.values()))
        return self.content.get(user_agent, [])

    def generate(self, output_path='.'):
        with open(f'{output_path}/robots.txt', 'w') as writer:
            for user_agent in self.user_agents():
                writer.write(f'User-agent: {user_agent}\n')
                for permission, endpoint in self.rules(user_agent):
                    writer.write(f'{permission}: {endpoint}')

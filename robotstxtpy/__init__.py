from itertools import chain


class RobotsTxt:

    def __init__(self):
        self.content = dict()

    def add_user_agent(self, user_agent):
        result = self.content.get(user_agent, None)
        if result is None:
            self.content[user_agent] = []

    def add_endpoint(self, user_agent, permission, endpoint):
        if user_agent not in self.content:
            self.add_user_agent(user_agent)
        self.content[user_agent].append((permission, endpoint))

    def user_agents(self):
        return list(self.content.keys())

    def rules(self, user_agent=None):
        if user_agent is None:
            return list(chain.from_iterable(self.content.values()))
        return self.content.get(user_agent, [])


def generate_robotstxt(output_path, robotstxt):
    with open(f'{output_path}/robots.txt', 'w') as writer:
        for user_agent in robotstxt.user_agents():
            writer.write(f'User-agent: {user_agent}\n')
            for permission, endpoint in robotstxt.rules(user_agent):
                writer.write(f'{permission}: {endpoint}')

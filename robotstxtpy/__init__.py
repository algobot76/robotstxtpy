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

    @property
    def user_agents(self):
        return list(self.content.keys())

    @property
    def endpoints(self):
        return list(chain.from_iterable(self.content.values()))

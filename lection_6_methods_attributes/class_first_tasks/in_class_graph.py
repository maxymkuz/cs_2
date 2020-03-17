class User:
    count = 0

    def __init__(self, username, password):
        self.password = password
        self.username = username
        User.count += 1

    def status(self):
        pass

    @staticmethod
    def count_users():
        return User.count


class Admin(User):
    def status(self):
        return "Admin"


class Editor(User):
    def status(self):
        return "Editor"


class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = {}


class GraphPass:
    def graph_pass(self, g):
        raise NotImplementedError


class BFS(GraphPass):
    def graph_pass(self, g):
        pass


class BFS(GraphPass):
    def graph_pass(self, g):
        pass

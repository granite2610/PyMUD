import uuid


class BaseClient(object):
    def __init__(self):
        self.uuid = uuid.uuid4()

    def check_for_messages(self):
        pass


class Client(BaseClient):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        # TODO: I just want a client to represent a socket initially
        self.name = None
        self.player = None
        self.room = None

    def check_for_messages(self):
        return self.socket.check_for_messages(self)


class NpcClient(BaseClient):
    def __init__(self):
        super().__init__()

    def check_for_messages(self):
        pass
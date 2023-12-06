import datetime


class Node:
    def __init__(self, id: int, title: str, body: str, editAt: datetime):
        self.id = id
        self.title = title
        self.body = body
        self.editAt = editAt

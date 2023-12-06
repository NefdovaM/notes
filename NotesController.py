import datetime
import json
from typing import Optional, Any

from Node import Node


def loadFromFile() -> [Node]:
    with open("database.json", "r") as read_file:
        return json.load(read_file, object_hook=lambda d: Node(**d))


LIST_OF_NODES: [Node] = loadFromFile()


def get_all_notes() -> [Node]:
    return LIST_OF_NODES


def get_by_date(date_time: datetime):
    print("inputted " + date_time.__str__())


def is_node_exist(id: int) -> bool:
    for item in LIST_OF_NODES:
        if item.id == id:
            return True
    return False


def drop_node(id: int) -> Node:
    targetNode = get_node(id)
    LIST_OF_NODES.remove(targetNode)
    return targetNode


def get_node(id: int) -> Node:
    for item in LIST_OF_NODES:
        if item.id == id:
            return item
    return None

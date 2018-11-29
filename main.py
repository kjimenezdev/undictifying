#!/usr/bin/env python
"""The purposeof this script is to create a parsing comparison between
undictify and schematics

Author: Konrad Jimenez <kjimenez@keplergrp.com>
"""
from typing import NamedTuple
from schematics.models import Model
from schematics.types import (
    StringType,
    BooleanType,
    IntType,
)
import requests
from undictify import (
    type_checked_constructor,
    type_checked_call,
)

# pylint: disable=too-few-public-methods

ENDPOINT = "https://jsonplaceholder.typicode.com/todos/1"


@type_checked_constructor()
class UndictTodo(NamedTuple):
    """Basic namedtuple"""
    id: int
    userId: int
    title: str
    completed: bool

# @type_checked_constructor()


class SchematicsTodo(Model):
    """Basic schematics model"""
    id = IntType(required=True)
    userId = IntType(required=True)
    title = StringType(required=True)
    completed = BooleanType(required=True)


class Todo():
    """Todo"""

    def __init__(self, id, userId, title, completed):
        self.id = id
        self.userId = userId
        self.title = title
        self.completed = completed

    @classmethod
    def checked_from_dict(cls, data: dict)-> 'Todo':
        """Checks types from a dict"""
        if not isinstance(data["id"], int):
            raise TypeError("ERROR id is not an integer")
        if not isinstance(data["userId"], int):
            raise TypeError("ERROR userId not an integer")
        if not isinstance(data["title"], str):
            raise TypeError("ERROR title not a string")
        if not isinstance(data["completed"], str):
            raise TypeError("ERROR title not a string")
        return cls(
            data["id"],
            data["userId"],
            data["title"],
            data["completed"]
        )


def fetch_data(url: str) -> dict:
    """Fetchs data"""
    request = requests.get(url)
    return request.json()


def undict() -> None:
    """Undictify """
    print("Undictify testing")


@type_checked_call()
def target_function(id: int, userId: int, title: str, completed: bool):
    todo = Todo(id, userId, title, completed)
    print(todo)


def main()-> None:
    """Main method"""
    # data = fetch_data(ENDPOINT)
    data = {'userId': 1234, 'id': 1,
            'title': 'delectus aut autem', 'completed': False}
    # result = target_function(**data)
    # print(data)
    todo = Todo.checked_from_dict(data)
    print(todo)
    undict_todo = UndictTodo(**data)
    print(undict_todo)
    schems = SchematicsTodo(data)
    print(schems)


if __name__ == "__main__":
    main()

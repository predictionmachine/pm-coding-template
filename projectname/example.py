"""
Copyright (C) Prediction Machine Advisers, LLC - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by staff at Prediction Machine, January 2021

This file is an example of what a python file can look like
"""
from typing import List, NewType

# Use NewType to create meaningful distinct types, per https://docs.python.org/3/library/typing.html
UserId = NewType("UserId", int)
some_id = UserId(524313)


def foo(user_id: UserId) -> List[UserId]:
    return [user_id]

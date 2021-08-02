# Copyright (C) 2021 Prediction Machine Advisers, LLC - All Rights Reserved
# Unauthorized copying of this file via any medium is strictly prohibited
# Proprietary and confidential
# Written by staff at Prediction Machine

"""
This file deals with UserId

Provides support for listifying it, eg in service of having things as lists
"""
from typing import List, NewType

# Use NewType to create meaningful distinct types, per https://docs.python.org/3/library/typing.html
UserId = NewType("UserId", int)


some_id = UserId(524313)


def listify(user_id: UserId) -> List[UserId]:
    """Returns a list containing the single passed in UserId"""
    return [user_id]

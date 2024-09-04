#!/usr/bin/env python

from user import User

import random
knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


class Teacher(User):
    
    #initializing the Teachers class
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    #random.randit(minimum number, maximum number)- Return random integer in range [a, b], including both end points.
    def teach(self):
        return self.knowledge[random.randint(0, len(knowledge) -1)]
        



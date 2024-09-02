#!/usr/bin/env python

from user import User

import random

class Teacher(User):
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

    def teach(self):
        return random.choice(self.knowledge)
        pass
    def __str__(self):
        return (f"Teacher: {self.first_name} {self.last_name}, "
                f"Knowledge: {self.knowledge}")
    
teacher = Teacher("Jane", "Smith") 

print(teacher)  
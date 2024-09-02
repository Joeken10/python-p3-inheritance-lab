#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, knowledge_string):
        self.knowledge.append(knowledge_string)
        pass
    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Knowledge: {self.knowledge}"
    
    # Creating instances
student = Student("John", "Doe")


# Adding knowledge to the student
student.learn("Mathematics is fun.")

# Printing instances
print(student)


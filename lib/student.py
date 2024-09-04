#!/usr/bin/env python

from user import User

class Student(User):
    # initializing the student class
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
        
    
    def learn(self, student_knowledge):
        self.knowledge.append(student_knowledge)
        pass
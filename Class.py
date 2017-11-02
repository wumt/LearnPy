#!/usr/bin/env python
# coding=UTF-8
import types
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s::%s' % (self.name,self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson',99)

bart.print_score()
lisa.print_score()
print lisa.get_grade()
print bart.get_grade()
print Student



class Animal(object):
    def run(self):
        print 'Animal is running...'
class dog(Animal):
    def run(self):
        print 'Dog is running...'
class cat(Animal):
    def run(self):
        print 'Cat is running...'

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog())
print types.StringType
print dir('ABC')
print 'ABCD'.__len__()
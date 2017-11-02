from types import MethodType
class Student(object):
       __slots__ = ('name','age','_score')
       def get_score(self):
           return self._score

       def set_score(self, value):
           if not isinstance(value, int):
               raise ValueError('score must be an integer!')
           if value < 0 or value > 100:
               raise ValueError('score must between 0 ~ 100!')
           self._score = value
       def set_ages(self,age):
           self.age=age
s = Student()
s.set_score(11)

print s.get_score()

#
# s = Student()
# s.name = 'Alan'
# s.age = 22
#
# print s.name
# s.set_age = MethodType(set_ages, s, Student)
# s.set_age(25)
# print s.age
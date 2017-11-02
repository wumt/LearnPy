class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
print Student('AAlan')
print (type(Student))

Student('ZhaoSI')
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
print Chain().status.user.timeline

class Family(object):
    def __init__(self,name):
        self.name=name
    def __call__(self, *args, **kwargs):
        print ('my name is %s.'   % self.name)

z=Family('Alan')
print (type(z))
z()

print callable(Family('Alan'))
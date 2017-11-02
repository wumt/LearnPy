import os
import pickle
print os.name
# print os.environ
# print os.getenv('PATH')
# print os.path.abspath('.')

# os.path.join('f://','alan')
# os.mkdir('f://alan')
# os.rmdir('f://alan')
f = open('dump.txt', 'wb')
d = dict(name='Bob', age=20, score=88)
print pickle.dumps(d)
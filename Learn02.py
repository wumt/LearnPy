#!/usr/bin/env python
# coding=UTF-8
import sys
from PIL import Image
im = Image.open('13.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200,100))
im.save('thumb.png', 'PNG')
print sys.path
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
print_score(std1)
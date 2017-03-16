# -*- coding: utf-8 -*-
class A:
    def b(self):
        pass

if A.b is A.b:
    print("Python 3")
else:
    print("Python 2")
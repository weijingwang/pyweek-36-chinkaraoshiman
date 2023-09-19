import random

class Obj:
    def __init__(self):
        self.x = random.getrandbits(1)

a = Obj()
b = Obj()
c = Obj()

print(a.x, b.x, c.x)
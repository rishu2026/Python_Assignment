class A:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d

class B(A):
    a=1000
    c=43
    @classmethod
    def display(cls):
        print(cls.a)

obj1=B(1,2)
print(obj1.a)
print(obj1.b)
print(obj1.c)
print(obj1.d)

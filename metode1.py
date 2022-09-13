class SomeClass ():
    a=1
    b=3
    c=-4

    def method1 (self,x):
        return x*x+3*x-4

obj=SomeClass()
print(obj.method1(int(input("ievadiet x="))))


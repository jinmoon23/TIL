class Person:
    population = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def eat(self):
        print('밥을 먹는다.')

p1 = Person('wlsans',24)
p2 = Person('qottkf',29)
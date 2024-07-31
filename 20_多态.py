class Animals():
    def spark(self):
        pass

class Dog(Animals):
    def spark(self):
        print('汪汪汪')

class Cat(Animals):
    def spark(self):
        print('喵喵喵')

class Ji(Animals):
    def spark(self):
        print('咯咯咯')

dog = Dog()
dog.spark()
cat = Cat()
cat.spark()
ji =Ji()
ji.spark()

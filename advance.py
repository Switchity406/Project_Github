class Book:

    def __init__(self, name):
        self.name = name
        print('inside construction')


    def show(self):
        print('hello may name is ',self.name)


s1 =Book('chandan')
s1.show()
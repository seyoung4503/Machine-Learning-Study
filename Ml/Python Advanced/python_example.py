class Person:
    def __init__(self, name, age, height) -> None:
        '''
        Protected with one underscore
        Private with two underscore
        '''
        self.name = name
        self._height = height
        self.__age = age

    def print_age(self) -> None:
        return print(self.__age)
    

        

person = Person("kim", 20)
person.print_age()

person.__age += 1
person.print_age()



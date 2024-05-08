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
    
    def get_age(self) -> int:
        return self.__age
    
    def set_age(self, age) -> None:
        if age < 0 :
            raise ValueError("Invaild age")
        self.__age = age

    

        

person = Person("kim", 180, 20)
person.print_age()

# not available
# person.__age += 1
# person.print_age()

person.set_age(25)
new_age = person.get_age()
print(new_age)
# result : 25
person.print_age()
# result : 25


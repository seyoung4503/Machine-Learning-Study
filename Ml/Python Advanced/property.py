class Person:
    def __init__(self, first_name, second_name, age, height) -> None:
        '''
        Protected with one underscore
        Private with two underscore
        '''
        self.first_name = first_name
        self.second_name = second_name
        self._height = height
        self.__age = age

    def print_age(self) -> None:
        return print(self.__age)
    
    # def get_age(self) -> int:
    #     return self.__age
    
    # def set_age(self, age) -> None:
    #     if age < 0 :
    #         raise ValueError("Invaild age")
    #     self.__age = age
    
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, age) -> int:
        if age < 0 :
            raise ValueError("Invaild age")
        self.__age = age

    @property
    def full_name(self)-> str:
        return self.first_name + " " + self.second_name

    

        

person = Person("kim","lam", 20, 180)
person.print_age()

# not available
# person.__age += 1
# person.print_age()

# person.set_age(25)
# new_age = person.get_age()
# print(new_age)
# # result : 25
# person.print_age()
# # result : 25

# person.set_age(-1)
# person.print_age()
# # result raise error

print(person.age)
person.age += 1
print(person.age)

print(person.full_name)



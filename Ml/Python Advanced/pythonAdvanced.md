# Python Advanced 

> This document covers practical python examples.

* private, protected variable
> In python, it has been customary to add one underscore in front of protected variables and two underscore in front of private variables. 
'''python
    def __init__(self, name, age, height) -> None:
        '''
        Protected with one underscore
        Private with two underscore
        '''
        self.name = name
        self._height = height
        self.__age = age
'''
> In this example, we can confirm that _height declared as protected variable and also __age declared as private variable. However, this declaration is not strictly controlled. That means we can access the internal variables at any time, even if it is not desirable. 
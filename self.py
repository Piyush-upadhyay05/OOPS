# class Person:
#     def __init__(name, age):  # Missing self!
#         name = name
#         age = age
#        # If you create a Person object:
#         p = Person("Alice", 25)
#         print(p.name)
class Person:
    def __init__(self, name, age):
        self.name = name  # Assign name to the object's name attribute
        self.age = age    # Assign age to the object's age attribute
        p = Person("Alice", 25)
        print(p.name)  # Output: Alice
        print(p.age)   # Output: 25
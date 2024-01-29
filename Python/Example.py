# Performing Inheritance

# Parent Class Created
class ParentClass:

    def __init__(self, age, height):
        self.age = age
        self.height = height

    def emp(self):
        print(self.age, self.height)


# Child Class created, to inherit
class ChildClass(ParentClass):
    def __init__(self, age, height, name):
        # Call constructor for parent class
        super().__init__(age, height)
        self.name = name


# Object created
child_instance = ChildClass(91, 176, "Garvit")
print(child_instance.name)

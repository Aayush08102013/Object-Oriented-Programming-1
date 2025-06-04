# Project 1:

class Student():
    grade = 10
    print("Hello my grade is", grade)

ob = Student()


# Project 2:

class Vehicle():

    def __init__(self, max_speed, mileage):
        
        # blind arguments:
        self.max_speed = max_speed
        self.mileage = mileage
    
# Object creation:

modelx = Vehicle(240, 18)

# acess using the dot operator:
print("Model max speed:", modelx.max_speed)
print("Model mileage:", modelx.mileage)

# Project 3:

class Parrot():

    #class atribute:
    species = "bird"

    # instance atribute:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instancetiate the parrot class:

blu = Parrot("Blu", 17)
moo = Parrot("Moo", 15)

# acess the atribute:

print("Blu is a {}".format(blu.species))
print("moo is a {}".format(moo.species))

# acess the instance atribute:

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(moo.name, moo.age))


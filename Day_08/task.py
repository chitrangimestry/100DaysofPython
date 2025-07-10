#Function without Inputs
'''
def greet():
    print("Hello")
    print("This is function in Python.")
    print("Thank you, Goodbye!!!")

greet()

#function with Inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f'How are you doing {name}?')
    print(f"Thank you {name}, Goodbye!!!")
greet_with_name("Chitrangi")
#Function with more than one parameter
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")
greet_with("Jack Bauer", "Dublin, Ireland")
'''


def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")


greet_with(name="Jack Bauer", location="Ireland")

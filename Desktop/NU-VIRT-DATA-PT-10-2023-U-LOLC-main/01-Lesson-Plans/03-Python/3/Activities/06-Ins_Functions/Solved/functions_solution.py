# Basic Definition
def name(parameters):
    # code goes here
    return


# Simple Function with no parameters
def show():
    print(f"Hi!")


# you use parentheses to run the code in a function
show()


# Simple function with one parameter
def show(message):
    print(message)


# Think of the parameter `message` as a variable
# You assign the string "Hello, World!" when you call the function
# This is like saying `message = "Hello, World!"`
show("Hello, World!")


# Functions can have more than one parameter
def make_quesadilla(protein, topping):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)


# Supply the arguments (values) when calling the function
make_quesadilla("beef", "guacamole")
make_quesadilla("chicken", "salsa")

# @NOTE: Order is important when supplying arguments! you can define variables if you switch the original order
#make_quesadilla(topping = "sour cream", protein = "beef")
make_quesadilla("sour cream", "beef")


# We can also specify default values for parameters
def make_quesadilla(protein, topping="sour cream"):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)


# Make a quesadilla using the default topping
make_quesadilla("chicken")

# Make a quesadilla with a new topping
make_quesadilla("beef", "guacamole")


# Functions can return a value
def square(number):
    return number * number
# Functions can return a value of user input
def square():
    user_input = int(input('choose number'))
    answer = user_input * user_input
    return answer
print()
# You can save the value that is returned
squared = square(2)
print(squared)

# You can also just print the return value of a function
print(square(2))
print(square(3))

# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    #average = sum(numbers)/len(numbers) would also work
    total = 0.0
    number_of_elements= len(numbers)
    for x in numbers:
        total = total + x
    return total / number_of_elements


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))

user_play = "y"
start_number = 0

# While we are still playing...
while user_play == "y":
    #ask the user how many numbers to loop through
    user_number = int(input("How many numbers should we loop through?"))
    #loop through the numbers, cast string as integer

    for x in range(0, user_number + start_number):
        print(x)

#once complete...
    start_number = start_number = user_number

    user_play = input("Would you like to continue? (y)es or (n)o")

    #this formula isn't working properly
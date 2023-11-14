# Initialize variables 
shopping = 'y'

pie_list = ['Pecan', #0
            'Apple Crisp', #1 
            'Bean',  #2
            'Banoffee', 
            'Black Bun', 
            'Blueberry', 
            'Buko', 
            'Burek']

user_choices = []

print('Welcome to the House of Pies Here are our pies')
print('_______________________________________________________________')


# While we are still shopping
while shopping == 'y':
    print('(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek')
    choice = input('Which pie would you like to order?')

    user_choices.append(choice)

    print(f"Great! We'll have that {pie_list[int(choice) - 1]} right out to you.")

    shopping = input('Would you like to continue shopping? (y)es or (n)o')

print(f"You purchased a total of {str(len(user_choices))} pies.")


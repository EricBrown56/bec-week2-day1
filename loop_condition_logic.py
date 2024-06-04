# Loop condition exploration: Write a while loop with a condition that will never be true. Ask the user a question until their answer triggers a break statement.

yum = True

while yum:
    tacos = input('Do you like tacos? (yes/no)')
    if tacos == 'yes':
        yum = False
    if not yum:
        print('Great, I like tacos too!')


# Create a while loop that will terminate after 5 iterations. Print the current iteration number for each iteration.

pizza = []
# I can only eat 5 slices of pizza

while len(pizza) < 5:
    print('Eating a slice of pizza')
    pizza.append('Slice')
    print('Slices of pizza eaten:', len(pizza))

print("OMG I'm so stuffed!")

        


print('Welcome to the Letter Counter App')
#Get user in put
name = input('What is your name? ')
print(f'Hello {name}!')
phrase = input('/n Please enter a phrase and I will count the number of times a letter has occurred in it: ').lower()
letter = input('What letter do you want me to count? ').lower()
#Count letter occurunce
letter_count = phrase.count(letter)
#Output the results
print(f'Your letter has appeared {letter_count} times in your phrase')


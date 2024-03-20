
# Task 1
#
# string = "Spider-man, Ironman, Batman, Superman, Wonder Woman"
# list = string.split(',')
#
# for superhero in list:
#
#     print(superhero.strip())



# Task 2

# import random
# user_input = 0
# bot = random.randint(1, 20)
# while user_input != bot:
#     user_input = int(input('Enter some number from 1 to 20: \n'))
#     if user_input == bot:
#         print('You won!')
#     elif user_input < bot:
#         print('Your number is less. Try a higher number!')
#     else:
#         print('Your number is more. Try a lower number!')



# Task 3

# word = 'Programming is awesome!'
# list = []
# count = 0
# for letter in word:
#     list.append(letter)
# for char in list:
#     if char == 'a':
#         count += 1
# print(count)



# Task 3 (another way)

# word = 'Programming is awesome!'
# print(word.count("a")



# Task 4
#
# user_input = ""
# password = 'Admin123'
# count = 3
# while count > 0:
#     user_input = input('Enter password: \n')
#     if user_input == password:
#         print('You enter correct password!')
#         count = 0
#     elif count > 1:
#         print(f'Wrong password. You have {count - 1} attempt. Try again!')
#         count -= 1
#     else:
#         print('You loser')
#         count -= 1



# Task 5
#
# user_input = input("Enter a word or sentence: ")
# i = 0
# changed_input = []
# while i < len(user_input):
#     temp = user_input[i]
#     if temp.islower():
#         changed_input.append(temp.upper())
#     else:
#         changed_input.append(temp.lower())
#     i += 1
# print(''.join(changed_input))

import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the password generator!")

num_letter = int(input("Please enter the number of letters you want for password: "))
num_numbers = int(input("Please enter the number of numbers you want for password: "))
num_symbols = int(input("Please enter the number of symbols you want for password: "))


pwd_let = random.choices(letters, k=num_letter) + \
          random.choices(numbers, k=num_numbers) + \
          random.choices(symbols, k=num_symbols)

random.shuffle(pwd_let)


final_password = ''.join(pwd_let)

print("Your generated password is:", final_password)

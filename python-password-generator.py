import random
import string
#User input
length = int(input("Enter the length of the password: "))
#user Preference
use_upper = input("Do you want to make it in uppercase? (y/n): ")
use_numbers = input("Do you want to use numbers? (y/n): ")
use_symbols = input("Do you want to use symbols? (y/n): ")

#Generate password
characters = string.ascii_lowercase
password = ""

if use_upper == "y" :
    characters += string.ascii_uppercase

if use_numbers == "y" :
    characters += string.digits

if use_symbols == "y" :
    characters += string.punctuation

for i in range(length):
    password += random.choice(characters)

print("Generated password:" , password)
        

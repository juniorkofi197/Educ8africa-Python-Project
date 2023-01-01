import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){},;:.'_-/\\?+*#!@$%^&|"

upper,lower,nums,syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
    #this means if we chose to use uppercase letters meaning we are going to include them into the final string

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols

length = 12
amount = 7

for x in range(amount):
    password = "".join(random.sample(all,length))
    #random.sample means it's going to take random strings out of the full strings that wew have
    #join is a function
    #all means we are using all the strings we have defined at the top and length also means how long its going to be as we've defined as 12
    print(password)

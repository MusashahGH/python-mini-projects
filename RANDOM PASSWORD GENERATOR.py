# Mini Projects in Python
# Random Password Generator 

import random
import string #module collection of string constants

pass_len=8

# print(string.ascii_letters)  for samll n capital a to z
# print(string.digits) for 0 to 9
# print(string.punctuation) for all special charachter
#Now I merge it into a single string list

charValue=string.ascii_letters+ string.digits+ string.punctuation
password=""
for i in range(pass_len):
    password +=random.choice(charValue)

print("your random password is:",password)
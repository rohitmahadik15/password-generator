#-------Made by Rohit Mahadik-----#

#Generate random and unique Password
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "@#&*/\?"

add = lower_case + upper_case + numbers + symbols
length_for_pass = 8

generated_password = "".join(random.sample(add, length_for_pass))

print("Your UNIQUE password is : ", generated_password)
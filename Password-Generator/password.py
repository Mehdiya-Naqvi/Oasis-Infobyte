import random
chars = "abcdefghijklmnopqrstuvwxyz!@#$%&*()ABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789"
len = int(input("Enter the length of your Password :- "))
password = ""
for i in range(len):
    password+=random.choice(chars)
print(password)

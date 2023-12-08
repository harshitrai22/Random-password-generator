import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#syntax -> random.sample(Given sample, length)   - It Gives output in the form of list
p = "".join(random.sample(s,passlen ))
print(p)
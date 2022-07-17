#Write a Python program that accepts a word from the user and reverse it.S

name1=input("enter a string that need to be reversed : ")
name2=[]
for i in range(len(name1)-1,-1,-1):
    name2.append(name1[i])
print("reverse string is :","".join(name2))


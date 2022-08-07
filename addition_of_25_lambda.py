'''
Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

sample input: 10
sample output: 35
'''


num1 = 25
add = lambda num1,num2 : num1+num2 
num2=int(input("Enter number to be added with 25 :"))
result = add(num1,num2)
print("Result:",result)
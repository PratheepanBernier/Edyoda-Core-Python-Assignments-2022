'''
Write a Python program to triple all numbers of a given list of integers. Use Python map.

sample list: [1, 2, 3, 4, 5, 6, 7]

Triple of list numbers:

[3, 6, 9, 12, 15, 18, 21]
'''

lst=[]
lst_size = int(input("Enter the size of the list: "))
for i in range(lst_size):
    num1=int(input("Enter the numbers to be added in the list: "))
    lst.append(num1)

def multiply_three (lst):
    return lst*3
result = list(map(multiply_three,lst))
print("Values after multiplying with 3 : ",result)

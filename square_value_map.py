'''
Write a Python program to square the elements of a list using map() function.

Sample List: [4, 5, 2, 9]

Square the elements of the list: [16, 25, 4, 81]
'''

lst=[]
lst_size = int(input("Enter the size of the list: "))
for i in range(lst_size):
    num1=int(input("Enter the numbers to be added in the list: "))
    lst.append(num1)

def square_value(lst):
    return lst**2

square_val = list(map(square_value,lst))
print("Square values of the numbers : ",square_val)
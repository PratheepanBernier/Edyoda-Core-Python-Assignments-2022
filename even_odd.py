#Write a Python program to count the number of even and odd numbers from a series of numbers.
n1=int(input("enter the start value:"))
n2=int(input("enter the end value:"))
n4=0
n5=0
for n3 in range(n1,n2+1,1):
    if n3%2==0 :
        n4=n4+1
    else:
        n5=n5+1
print("Number of even numbers:",n4)
print("Number of odd numbers :",n5)



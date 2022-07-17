#Write a Python program to get the Fibonacci series between 0 to 50:

n1=1
n2=0
n3=0
for n3 in range(0,50,1):
    n3=n1+n2
    if n3<50:
        print(n3)
        n1=n2
        n2=n3

#since expected output starts from 1... i have done coding in such a way that it doesn't starts from 0.
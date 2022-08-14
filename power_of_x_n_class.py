"""Write a Python class to implement pow(x, n)

Explanation:
Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
You must implement it using Class

Sample Input:
x: 10
n: 2

Sample Output:
100
"""

#Program:

class power  :                                    #class initialisation
    def __init__(self):                           #constructor initialisation
        pass
    def pow(self,x,n):                            #method initialisation
        exponential=0
        n_value = n 
        x_value = x 
        exponential = x_value**n_value
        return exponential
x=int(input("Enter x value: "))
n=int(input("Enter n value: "))
obj = power()                                     #object declaration
answer = obj.pow(x,n)                             #method calling
print(f"{x} power {n} value is : {answer}")       #output print statement
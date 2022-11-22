'''
Find nth fibonacci number. If it starts with 0,1,1,2.....
Also, Print Incorrect Input if n is less than or equal to 0.

Input Format:
Call the function with n

Output Format:
Print the nth fibonacci number

Sample Input 0:
4

Sample Output 0:
2

Sample Input 1:
 0

Sample Output 1:
Incorrect input
'''

def fibonacci_nth_number(n_value) :
    if n_value != 0:
        fib=0
        fib1=1
        if n_value==1:
            print(fib)
        elif n_value==2:
            print(fib1)
        else:
            for _ in range(2,n_value):
                fib=fib+fib1
                fib,fib1=fib1,fib
            print(fib1)
    else:
        print("Incorrect input")

try:
    n_value = int(input(""))
    fibonacci_nth_number(n_value)
except:
    print("Invalid input")
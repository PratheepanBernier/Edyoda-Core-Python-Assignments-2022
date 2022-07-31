size1 = int(input("Enter the total numbers that needed to be added : "))
lst=[]
for i in range(1,size1+1):
    num1=int(input("enter number : "))
    lst.append(num1)
def suming(lst) :
    add1=0
    for i in range(0,size1,1) :
        add1 = add1 + lst[i] 
    return add1
print("Addition of numbers is : ",suming(lst))

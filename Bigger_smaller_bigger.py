'''
Q2. You will be given a list. You have to print a list whose 1st element should be largest and 2nd should be the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.

Input Format:
The first line will have space-separated elements of the list.

Output Format:
Print the required list.

Sample Input 0:
1 2 3 4 5 6

Sample Output 0:
6 1 5 2 4 3
'''

#Code:
list1 = input("").split(" ")
list2=[]
for values in list1:
    temp=int(values)
    list2.append(temp)
for values in range(len(list2)):
    if values%2==0:
        print(max(list2),end=" ")
        list2.remove(max(list2))
    else:
        print(min(list2),end=" ")
        list2.remove(min(list2))
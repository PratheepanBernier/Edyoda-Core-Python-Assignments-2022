'''
User can give any input as they wish . For example:

sample input:
4
great,hello,hiyo,abc

sample output:
['great', 'abc', 'hello','hiyo']

'''

try: 
    size = int(input(""))
    names = input("").split(",")
    if size==len(names):
        func_val = lambda name:name[-2]
        sorted_list=sorted(names,key = func_val )
        print(sorted_list)
    else:
        print("Invalid input")
except:
    print("Invalid Input")


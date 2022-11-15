'''
Inbuilt inputs given as per example inputs 
'''

names = ['great','hello','hiyo','abc']
func_val = lambda name:name[-2]
sorted_list=sorted(names,key = func_val)
print(sorted_list)
def  upper_lower_case_count(str1):
    upper_count = 0
    lower_count = 0
    space_count = 0
    for i in str1 :
        if i.isupper():
            upper_count=upper_count+1
            continue
        elif i == " " :
            space_count=space_count+1
            continue
        else :
            lower_count=lower_count+1
            continue
    print("No. of upper case letters is :", upper_count)
    print("No. of lower case letters is :",lower_count)

str1= input("Enter the string for checking upper/lower case count :")

upper_lower_case_count(str1)
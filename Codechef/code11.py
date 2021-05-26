T = int(input())
while T!=0:
    num =int(input())
    str_obj = str(num)
    count_3 = str_obj.count('3')
    count_7 = str_obj.count('7')
    if count_7+count_3==len(str_obj):
        print("LUCKY")
    else:
        print("BETTER LUCK NEXT TIME")        
    T-=1
T = int(input())
first_lang =[chr(c) for c in range(97,110)]
second_lang =[chr(c) for c in range(78,91)]
while T!=0:
    count =0
    flag =0
    arr = list(input().split())
    nums = int(arr.pop(0))
    for word in arr:
        if word.islower():
            for v in word:
                if v in first_lang:
                    continue
                else:
                    flag =1
            if flag==0:
                count+=1
            else:
                break
        elif word.isupper():
            for v in word:
                if v in second_lang:
                    continue
                else:
                    flag =1
            if flag==0:
                count+=1
            else:
                break
    if count == nums:
        print("YES")
    else:
        print("NO")
    T-=1
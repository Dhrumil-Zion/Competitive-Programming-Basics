t = int(input())
while t!=0:
    sal = int(input())
    if sal<1500:
        final_sal =  sal+ (sal*0.1)+(sal*0.9)
    else:
        final_sal =  sal+ 500+(sal*0.98)
    print(final_sal)
    t-=1

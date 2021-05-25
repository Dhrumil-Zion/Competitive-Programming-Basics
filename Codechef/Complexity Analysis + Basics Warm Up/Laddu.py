# 2
# 4 INDIAN
# CONTEST_WON 1
# TOP_CONTRIBUTOR
# BUG_FOUND 100
# CONTEST_HOSTED
# 4 NON_INDIAN
# CONTEST_WON 1
# TOP_CONTRIBUTOR
# BUG_FOUND 100
# CONTEST_HOSTED

T = int(input())
while (T!=0):
    totalpoints = 0
    activities,origin = input().split()
    for _ in range(int(activities)):
        main_activity = input().split()
        if main_activity[0]=="CONTEST_WON":
            if int(main_activity[1])<21:
                totalpoints+=300+(20-int(main_activity[1]))
            else:
                totalpoints+=300
        elif main_activity[0]=="TOP_CONTRIBUTOR":
            totalpoints+=300
        elif main_activity[0]=="BUG_FOUND":
            totalpoints+=int(main_activity[1])
        elif main_activity[0]=="CONTEST_HOSTED":
            totalpoints+=50
    if origin=="INDIAN":
        print(totalpoints//200)
    elif origin=="NON_INDIAN":
        print(totalpoints//400)
    T-=1
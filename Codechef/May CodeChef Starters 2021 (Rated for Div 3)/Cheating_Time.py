T =int(input())
m=0
for _ in range(T):
    no_of_sir,time_for_passing,total_time = map(int,input().split())
    temp = []
    V = []
    time_consumption = 0
    for _ in range(no_of_sir):
        s,e =map(int,input().split())
        time_consumption+=len(range(s,e))
        temp.append([s,e])
    if time_for_passing==total_time or time_for_passing>total_time:
        print("NO")
        continue
    for c in range(1,len(temp)):
        ideal_time = temp[c][0]-temp[c-1][-1]
        V.append(ideal_time)
    ideal_time =max(V)
    if (
        time_consumption + ideal_time < total_time
        and total_time - (time_consumption + ideal_time) >= time_for_passing
        or time_consumption + ideal_time >= total_time
        and ideal_time >= time_for_passing
    ):
        print("YES")
    else:
        print("NO")



# T =int(input())
# while T!=0:
#     no_of_sir,time_for_passing,total_time = map(int,input().split())
#     for num in range(no_of_sir):
#         s,e =map(int,input().split())
#         total_time-=len(range(s,e))
#     if total_time>=time_for_passing:
#         print("YES")
#     else:
#         print("NO")
#     T-=1


T = int(input())
while T!=0:
    total_days,days_interval,per_day,increa_by = map(int,input().split())
    last_count = 0
    terms = total_days//days_interval
    total_days-=terms*days_interval
    if total_days>0:
        last_count =  per_day+ (increa_by*terms)
    previous_terms =  per_day + (increa_by*(terms-1))
    print(days_interval*(terms*(per_day+previous_terms)//2)+(last_count*total_days))
    T-=1



# T = int(input())
# while T!=0:
#     total_days,days_interval,per_day,increa_by = map(int,input().split())
#     total_till_date = per_day*days_interval
#     rate = 1
#     for _ in range(1,total_days,days_interval):
#         total_days-=days_interval
#         days = min(total_days, days_interval)
#         rate_per_day = rate+increa_by
#         rate = rate_per_day
#         total_till_date+=rate*days
#     print(total_till_date)
#     T-=1
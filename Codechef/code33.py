# First line will contain T, number of testcases. Then the testcases follow.
# Each testcase contains of three lines of input.
# First-line has two integer N,M.
# Second-line with N space-seperated number.
# Third-line with M space-seperated number.

T = int(input())
while T!=0:
    N,M = map(int,input().split())
    N_arr = set(map(int,input().split()))
    M_arr = set(map(int,input().split()))
    final_arr = N_arr.intersection(M_arr)
    temp = [c for c in final_arr if c%3==0]
    
    T-=1
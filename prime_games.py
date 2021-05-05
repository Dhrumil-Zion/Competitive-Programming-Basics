def main(): 
    T = int(input())
    for _ in range(T):

        lower,upper = input().split()
        l =int(lower)
        n = int(upper)+1

        sieve = [True] * n
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        arr = [2] + [i for i in range(3,n,2) if sieve[i]]

        lower = arr[min(range(len(arr)), key = lambda i: abs(arr[i]-l))]
        if lower < l:
            updated_arr = arr[arr.index(lower)+1:]
        else:
            updated_arr = arr[arr.index(lower):]

        n=len(updated_arr)        
        if n>1:            
            print(updated_arr[-1]-updated_arr[0])        
        elif n==1:            
            print(0)        
        elif n<1:            
            print(-1)
main()



# def main():
#     T = int(input())
#     while T!=0:
#         lower,upper = input().split()
#         temp = []
#         for num in range(int(lower), int(upper) + 1):
#             if num > 1:
#                 for i in range(2, num):
#                     if (num % i) == 0:
#                         break
#                 else:
#                     temp.append(num)
#         if len(temp) == 1:
#             print(0)
#         elif len(temp) > 1:
#             print(max(temp)-min(temp))
#         elif len(temp) <1:
#             print(-1)
#         T-=1

# main()

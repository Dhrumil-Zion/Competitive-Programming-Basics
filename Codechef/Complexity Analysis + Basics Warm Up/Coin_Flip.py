# Problem Name: Coin Flip 
# Problem Code: CONFLIP

T = int(input())

for _ in range(T):
    games = int(input())
    for _ in range(games):
        I,N,Q = map(int,input().split(" "))
        if N % 2 != 0 and I == Q or N % 2 == 0:
            print(int(N/2))
        else:
            print(int(N/2)+1)
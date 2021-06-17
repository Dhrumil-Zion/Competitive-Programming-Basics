T=int(input())
while T!=0:
    i = input().lower()
    if i=='b':
        print("BattleShip")
    elif i=='c':
        print("Cruiser")
    elif i=='d':
        print("Destroyer")
    elif i=='f':
        print("Frigate")
    T-=1
arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], 
        [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
z = []

initial_outer = 0
final_outer = 3

initial=0
final =3
ans = []

while 1:
    if final_outer==7:
        break
    while 1:
        if final ==7:
            break    
        for c in range(initial_outer,final_outer):
            for g in range(initial,final):
                z.append(arr[c][g])
        z.pop(3)
        z.pop(4)
        ans.append(sum(z))
        z.clear()
        initial +=1
        final+=1
    final = 3
    initial =0
    initial_outer+=1
    final_outer+=1

print(max(ans))
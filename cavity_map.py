# https://www.hackerrank.com/challenges/cavity-map/problem

grid = ['1112', '1912', '1892', '1234']
temp = [max(list(c)) for c in grid]
final = []
for f in grid:
    if max(temp) in f:
        final.append(f.replace(str(max(temp)), 'X'))
    else:
        final.append(f)
print(final)

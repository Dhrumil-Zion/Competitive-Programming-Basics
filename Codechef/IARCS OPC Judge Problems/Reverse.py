number_of_lines = int(input())
a = []
c = ["'", ".", ",", ";", ":"]
for _ in range(number_of_lines):
    line = input()
    for i in c:
        line = line.replace(i, " ")
    a.append(line)
for i in reversed(a):
    print(" ".join(reversed(i.split())))
ans = []

def arr_generation(st):
    numbers = st.split('=')
    f = [int(c) for c in numbers[0]]
    for c in range(1,len(numbers[0])):
        f.append(int(numbers[0][:c]))
    return list(set(f))

def subset_sum(numbers, target,partial=[]):
    global ans
    s = sum(partial)
    if s == target: 
        # print("sum(%s)=%s" % (partial, target))
        ans.append(len(partial)-1)
    if s >= target:
        return  
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 

st = "164=20"
subset_sum(arr_generation(st),20)
print(min(ans))

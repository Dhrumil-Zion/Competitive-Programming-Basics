
# Optimized solution , Easy to understand by https://leetcode.com/saichandugudala

def reverseBits(n):
    res=0
    for i in range(32): # since it is 32 bit integer
        res=res<<1   # left shift to check it till 32 bits
        res+=n%2  # checking if rightmost bit of n is 1 and adding to result
        n=n>>1     # checking all bits of n till n becomes 0
    return res

print(reverseBits(1001001010010))
## my way but will not be accepted by leetcode
n = "00000010100101000001111010011100"
print(int(n[::-1],2))

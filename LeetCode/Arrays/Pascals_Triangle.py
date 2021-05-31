def generate(numRows):
    triangle=[]
    for row in range(1,numRows+1):
        a=[1]*row
        triangle.append(a)
    for row in range(numRows):
        for col in range(1,row):
            triangle[row][col]=triangle[row-1][col-1]+triangle[row-1][col]
    return triangle
print(generate(5))
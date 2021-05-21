class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle=rectangle
        print(self.rectangle)


    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
            for i in range(row1,row2+1):
                for j in range(col1,col2+1):
                    self.rectangle[0][i][j]=newValue


    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
        

rectangle =[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]]

row1=3
col1 = 0 
row2 = 3
col2= 2
newValue = 10
row =0
col =2
obj = SubrectangleQueries(rectangle)
obj.updateSubrectangle(row1,col1,row2,col2,newValue)
param_2 = obj.getValue(row,col)
print(rectangle)
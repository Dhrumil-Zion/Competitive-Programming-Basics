import numpy as np
matrix = [[1,2,3],[4,5,6],[7,8,9]]
temp = []

ans = np.transpose(matrix)
print(ans)

## this java solution is 99% faster than python

# class Solution {
#     public int[][] transpose(int[][] matrix) {
#         int[][] ans = new int[matrix[0].length][matrix.length];
#         for(int i=0;i<matrix.length; i++){
#         for(int j=0; j<matrix[0].length; j++){
#             ans[j][i] = matrix[i][j];
#         }
#     }
#     return ans;
        
#     }
# }


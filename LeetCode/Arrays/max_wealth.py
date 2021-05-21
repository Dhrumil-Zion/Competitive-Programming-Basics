accounts = [[2,8,7],[7,1,3],[1,9,5]]
temp = [sum(c) for c in accounts]
print(max(temp))


## java 100% faster 

# class Solution {
#     public int maximumWealth(int[][] accounts) {
#      int wealth=0;
#      int max_wealth=0;
#         for(int i =0;i<accounts.length;i++){
#             for(int j=0;j<accounts[0].length;j++){
#                 wealth=wealth+accounts[i][j];
#                 max_wealth=Math.max(max_wealth,wealth);
#             }
#             wealth=0;
#         }
#         return max_wealth;
#     }
# }
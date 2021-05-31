T = int(input())
for _ in range(T):
    a,b,c,d,k= map(int,input().split())
    total = abs(a-c) + abs(b-d)
    if total>k:
        print("NO")
        continue
    else:
        fuel_left = k - total
        if fuel_left%2==0:
            print("YES")
        else:
            print("NO")

# #include<bits/stdc++.h>
# using namespace std;

# int main() {
# 	int testcase;
# 	for(cin>>testcase; testcase--;) {
# 		long long int tom_x, tom_y, jerry_x, jerry_y, fuel;
# 		cin>>tom_x>>tom_y>>jerry_x>>jerry_y>>fuel;
# 		long long int x = abs(tom_x - jerry_x), y = abs(tom_y - jerry_y);
# 		long long int total_fuel_consumed = x + y;
# 		if (total_fuel_consumed > fuel) {
# 			cout<<"NO\n";
# 			continue;
# 		}
# 		long long int fuel_left = fuel - total_fuel_consumed;
# 		if (fuel_left % 2 == 0) {
# 			cout<<"YES\n";
# 		} else {
# 			cout<<"NO\n";
# 		}
# 	}
# 	return 0;
# }
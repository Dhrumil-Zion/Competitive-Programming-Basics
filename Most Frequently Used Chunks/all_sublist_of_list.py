from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(len(my_list)+1):
		temp = [list(x) for x in combinations(my_list, i)]
		if temp:
			subs.extend(temp)
	return subs

print(sub_lists([1,2,3,4,5]))
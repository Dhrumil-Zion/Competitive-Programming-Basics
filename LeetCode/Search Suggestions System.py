products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
products = ["havana"]
searchWord = "tatiana"
temp_arr = []
final_arr =[]
if len(products)==1 and products[0][0]!=searchWord[0]:
    for _ in range(len(searchWord)):
        final_arr.append([])
else:        
    for id, _ in enumerate(range(len(searchWord)), start=1):
        st = searchWord[:id]
        for words in products:
            if words[:id] == st:
                temp_arr.append(words)
        temp_arr.sort()
        final_arr.append(temp_arr[:3])
        temp_arr.clear()
print(final_arr)


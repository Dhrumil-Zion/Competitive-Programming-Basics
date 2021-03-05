def position(arr):
   minimum = arr.index(min(arr))
   maximum = arr.index(max(arr)) 
   print ("The maximum is {} at position:: {}".format(max(arr),maximum + 1)) 
   print ("The minimum is {} at position:: {}".format(min(arr), minimum + 1))

arr = [123132,43543,2342432,56456,23423,12312,45654,654,2342,567856,3234234,234234657,7567564534]
position(arr)
i = input().split()
amt = int(i[0])
bal = float(i[1])
if amt%5 != 0 or amt+0.5 > bal:
    print ("%.2f" % float(bal))
else:
    print ("%.2f" % float(bal-amt-0.5))
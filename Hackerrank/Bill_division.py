def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    x  = int(sum(bill)/2)
    if abs(x-b) == 0:
        print("Bon Appetit")
    else:
        print(abs(x-b))
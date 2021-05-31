t =int(input())
while t!=0:
    no_of_gift,toal_turns_for_each = map(int,input().split())
    gift = list(map(int,input().split()))
    gift2 =gift.copy()
    turn =0
    chef_bag = []
    twin_bag =[]
    for c in range(2*toal_turns_for_each+1):
        if c == (2*toal_turns_for_each - 2):
            twin_bag.append(gift.pop(gift.index(max(gift))))
            twin_bag.append(gift.pop(gift.index(max(gift))))
            break
        if turn%2==0:
            chef_bag.append(gift.pop(gift.index(max(gift))))
        else:
            twin_bag.append(gift.pop(gift.index(max(gift))))
        turn+=1
    turn =0
    chef_bag_2 = []
    twin_bag_2 =[]
    for c in range(2*toal_turns_for_each+1):
        if c == (2*toal_turns_for_each - 2):
            chef_bag_2.append(gift.pop(gift.index(max(gift))))
            chef_bag_2.append(gift.pop(gift.index(max(gift))))
            break
        if turn%2==0:
            twin_bag_2.append(gift2.pop(gift2.index(max(gift2))))
        else:
            chef_bag_2.append(gift2.pop(gift2.index(max(gift2))))
        turn+=1
    print(max(sum(chef_bag_2),sum(chef_bag)))
    t-=1
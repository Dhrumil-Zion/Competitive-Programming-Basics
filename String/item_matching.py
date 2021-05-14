items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
index = -1
if ruleKey == "color":
    index=1
elif ruleKey == "name":
    index=2
elif ruleKey == "type":
    index=0
c = sum(f[index]==ruleValue for f in items)
print(c)
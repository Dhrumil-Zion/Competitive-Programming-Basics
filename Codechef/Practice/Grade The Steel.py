t =int(input())
def hardness_check(n):
    return n>50
def carbon_check(n):
    return n<0.7
def tensile_check(n):
    return n>5600

while t!=0:
    hardness,carbon,tensile =map(float,input().split())
    if hardness_check(hardness) and carbon_check(carbon) and tensile_check(tensile):
        grade = 10
    elif hardness_check(hardness) and carbon_check(carbon):
        grade = 9
    elif tensile_check(tensile) and carbon_check(carbon):
        grade = 8
    elif tensile_check(tensile) and hardness_check(hardness):
        grade = 7
    elif hardness_check(hardness) or carbon_check(carbon) or tensile_check(tensile):
        grade = 6
    else:
        grade = 5
    print(grade)
    t-=1
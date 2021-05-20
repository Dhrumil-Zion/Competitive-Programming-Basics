import math
def is_smart_number(num):
    val = int(math.sqrt(num))
    return num / val**2 == 1
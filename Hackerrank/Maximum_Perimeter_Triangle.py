from itertools import combinations
def maximumPerimeterTriangle(sticks):
    pairs = set(combinations(sticks, 3))
    selectedpair = None
    max = 0
    for pair in pairs:
        if (
            pair[0] + pair[1] > pair[2]
            and pair[0] + pair[2] > pair[1]
            and pair[1] + pair[2] > pair[0]
            and max < sum(pair)
        ):
            max = sum(pair)
            selectedpair = pair
    if selectedpair:
        selectedpair = list(selectedpair)
        selectedpair.sort()
        return selectedpair
    return [-1]
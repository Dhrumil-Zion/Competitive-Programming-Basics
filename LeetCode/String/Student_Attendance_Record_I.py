s = "PPALLP"

def checkRecord(self, s: str) -> bool:
    if s.count('A')<2 and s.count('L')<3:
        return True
    elif s.count('A')<2 and s.count('L')>2:
        for c in range(3,s.count('L')+1):
            temp ='L'*c
            if temp in s:
                return False
        return True
    else:
        return False


def checkRecord(self, s: str) -> bool:
    if s.count('A')<2 and s.count('L')<3:
        return True
    elif s.count('A')<2 and s.count('L')>2 and 'LLL' not in s:
        return True
    else:
        return False
        

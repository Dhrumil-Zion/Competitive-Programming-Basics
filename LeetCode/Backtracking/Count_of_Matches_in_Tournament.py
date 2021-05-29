## after geeting patter by solving problem i got that ans is nothing but n-1 always.

def numberOfMatches(n):
    return n-1   

## previous aaproach to get pattern 

def numberOfMatches(n):
    teams_left = n 
    total_matches = 0
    
    while teams_left>1:
        n_matches = teams_left//2 
        total_matches += n_matches
        teams_left -=n_matches 
        
    return total_matches   
print(numberOfMatches(100))
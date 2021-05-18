text = "loonbalxballpoon"        

res = {'b':text.count('b'), 'a':text.count('a'), 'l':text.count('l'), 'o':text.count('o'), 'n':text.count('n')}
if text is None or len(text) == 0:
    print(0)

min_ban = min(res.get('b'),res.get('a'),res.get('n'))
min_lo = min(res.get('l'),res.get('o'))//2

print(min(min_ban,min_lo))
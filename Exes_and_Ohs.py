def xo(s):
    x_counter = 0
    o_counter = 0
    s = s.lower()
    
    for i in s:
        if i == 'x':
            x_counter += 1
        if i == 'o':
            o_counter += 1
    
    if x_counter == o_counter:
        return True
    else:
        return False
    
#lepsze rozwiązanie
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
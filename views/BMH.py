def bmh(text, pattern):
    n, m = len(text), len(pattern)
    
    _m = m-1
    bad_chars={}
    for c in pattern:
        bad_chars[c] = _m
        _m -= 1
       
    i=0
    while i <= n-m:
        j = m-1
        while j >= 0 and text[i+j] == pattern[j]: j-= 1
        if j < 0: return i
        
        try:
            i += bad_chars.get(text[i+j])
        except:
            i += m-1
        
    return -1

def hamming(s1, s2):
    if len(s1) != len(s2):
        raise Exception("Strings must be equal lenght")
        
    sumatoria = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            sumatoria +=1
            
    return sumatoria


            
        
    
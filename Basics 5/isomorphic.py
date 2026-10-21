def IsIsomorphic(s: str, t:str)-> bool:
    if len(s)!=len(t):
        return False
    d1 = {}
    d2 = {}
    for i in range(len(s)):
        if s[i] and d1[s[i]] != t[i]:
            return False
        if t[i] and d2[t[i]] != s[i]:
            return False
        d1[s[i]] = t[i]
        d2[t[i]] = s[i]
    return True
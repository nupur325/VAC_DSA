#first non repeating character
def firstNotRepeating(s):
    d = {}
    count = 0
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]]= 1
    for i in range(len(s)):
        if d[s[i]] == 1:
            return s[i]
    return ""

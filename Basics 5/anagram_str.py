#check if two string are anagram
def anagram(n1:int,n2:int)-> bool:
    if sorted(str(n1)) == sorted(str(n2)):
        return True
    else:
        return False
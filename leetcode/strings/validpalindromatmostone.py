def validpalin(s):
    i,j = 0, len(s)-1
    while i<j:
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            return validpalutil(s, i+1, j) or validpalutil(s, i, j-1)
    return True

def validpalutil(s, i, j):
    while i<j:
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            return False
    return True

def validpalindrom(s):
    def ispalin(s, deleted=False):
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                if deleted:
                    return False
                return ispalin(s[i+1:len(s)-i], True) or ispalin(s[i:len(s)-i-1], True)
        return True
    return ispalin(s)

print(validpalin("abaxc"))
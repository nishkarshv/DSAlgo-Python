def isparanthesis(s):
    return ((s == '(') or (s == ')'))


def isvalidstring(s):
    c = 0
    for i in range(len(s)):
        if s[i] == '(':
            c += 1
        elif s[i] == ')':
            c -= 1
            if (c < 0):
                return False
    return (c == 0)


def removeInvalidParentheses(s):
    visit = {s}
    while True:
        valid = []
        for elem in visit:
            if isvalidstring(elem):
                valid.append(elem)
        if valid:
            return valid
        new_level = set()
        print("visit", visit)
        for elem in visit:
            for i in range(len(elem)):
                new_level.add(elem[:i]+elem[i+1:])
                print("newlevel", new_level)
        visit = new_level


# Driver Code
expression = ")("
print(removeInvalidParentheses(expression))
expression = "(a)())()"
print(removeInvalidParentheses(expression))

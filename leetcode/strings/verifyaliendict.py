def isAlienSorted(words, order):
    ordersindex = {c:i for i, c in enumerate(order)}
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        print(word1, word2)
        for k in range(min(len(word1), len(word2))):
            if word1[k] != word2[k]:
                if ordersindex[word1[k]] > ordersindex[word2[k]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False
    return True

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order))
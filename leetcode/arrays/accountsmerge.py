import collections
def accountsMerge(accounts):
    emailtoname = {}
    dfsgraph = collections.defaultdict(set)
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            dfsgraph[acc[1]].add(email)
            dfsgraph[email].add(acc[1])
            emailtoname[email] = name


    reslist = []
    seen = set()
    for email in dfsgraph:
        if email not in seen:
            seen.add(email)
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for n in dfsgraph[node]:
                    if n not in seen:
                        seen.add(n)
                        stack.append(n)
            reslist.append([emailtoname[email]]+ sorted(component))
    return reslist
    
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(accountsMerge(accounts))
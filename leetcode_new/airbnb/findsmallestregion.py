def findsmallestregion(regions, region1, region2):
    parents = {}
    for region in regions:
        parent = region[0]
        for i in region[1:]:
            parents[i] = parent
    ancester = {region1}
    
    while region1 in parents:
        region1 = parents[region1]
        ancester.add(region1)
    while region2 not in ancester:
        region2 = parents[region2]
    
    return region2
    
regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]]
region1 =  "Canada"
region2 = "South America"
print(findsmallestregion(regions, region1, region2))
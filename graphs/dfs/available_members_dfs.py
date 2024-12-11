"""
TeamsSupporters map is given to you. There is also FolksAvailable-array who are Available in office today. List all the Teams who have 100% support available today

Sample 1:
TeamsToSupporterMap = {
    "Thunders" : ["David", "Catherine"]
}
FolksAvailable = ["Catherine", "David", "Sam"]

Output: ["Thunders"]

Sample 2:
TeamsToSupporterMap = {
    "Thunders" : ["David", "Catherine"],
    "Warriors": ["Rebooters", "Sam", "Thunders"],
    "Rebooters": ["Thunders", "Sam"]
}
FolksAvailable =  ["Catherine","David","Sam"]

Output: ["Thunders","Warriors","Rebooters"]
"""


def full_availability(TeamsToSupporterMap, FolksAvailable):
    res = []

    def dfs(team, seen):
        # root = team
        # if team in seen:
        #     return False  # cycle detected
        # seen.add(team)

        for supporter in TeamsToSupporterMap.get(team, []):
            if supporter in TeamsToSupporterMap:
                # this support is a team, so recursively call dfs
                if not dfs(supporter, TeamsToSupporterMap):  # seen.add(supporter)
                    return False
            else:
                if supporter not in FolksAvailable:
                    return False
        # seen = set()
        return True
        # return False

    for team in TeamsToSupporterMap:
        seen = set()
        if dfs(team, seen):
            res.append(team)

    return res


if __name__ == "__main__":
    TeamsToSupporterMap = {
        "Thunders": ["David", "Catherine"],
        "Warriors": ["Rebooters", "Sam", "Thunders"],
        "Rebooters": ["Thunders", "Sam"],
    }
    FolksAvailable = ["Catherine", "David", "Sam"]
    print(full_availability(TeamsToSupporterMap, FolksAvailable))

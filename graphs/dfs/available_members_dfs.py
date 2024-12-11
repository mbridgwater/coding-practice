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

    def dfs(team, TeamsToSupporterMap):
        # root = team
        # if team not in seen:
        for supporter in TeamsToSupporterMap[team]:
            if supporter in TeamsToSupporterMap:
                # this support is a team, so recursively call dfs
                dfs(supporter, TeamsToSupporterMap)  # seen.add(supporter)
            else:
                if supporter in FolksAvailable:
                    return True
                else:
                    return False
        # return False

    for team in TeamsToSupporterMap:
        # seen = set()
        if dfs(team, TeamsToSupporterMap):
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

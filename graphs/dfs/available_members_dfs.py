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


def full_availability_cycles(TeamsToSupporterMap, FolksAvailable):
    res = []

    cache = {}

    def dfs(team, seen):
        """This dfs algorithm accounts for caching and cycles"""
        if team in seen and team not in cache:
            print("cycle detected")
            return False  # cycle detected
        if team in cache:
            return cache[team]

        seen.add(team)

        for supporter in TeamsToSupporterMap.get(team, []):
            if supporter in TeamsToSupporterMap:
                # this support is a team, so recursively call dfs
                if not dfs(supporter, seen):
                    cache[team] = False
                    return False
            else:
                if supporter not in FolksAvailable:
                    cache[team] = False
                    return False
        seen = set()
        cache[team] = True
        return True

    for team in TeamsToSupporterMap:
        """
        In total, this is an O(N) algorithm, where N is the number of teams and we assume each team has some constant number of supporters.
        Although it appears we are calling dfs N times (where dfs is an O(N) algorithm), we only build the graph once and use memoization so
        that in reality, dfs is only run once through the whole graph.
        """
        seen = set()
        if dfs(team, seen):
            res.append(team)

    return res


def full_availability_no_cycles(TeamsToSupporterMap, FolksAvailable):
    res = []

    cache = {}

    def dfs(team):
        """This dfs algorithm accounts for caching, but not for cycles"""
        if team in cache:
            return cache[team]

        for supporter in TeamsToSupporterMap.get(team, []):
            if supporter in TeamsToSupporterMap:
                # this support is a team, so recursively call dfs
                if not dfs(supporter):
                    cache[team] = False
                    return False
            else:
                if supporter not in FolksAvailable:
                    cache[team] = False
                    return False
        cache[team] = True
        return True

    for team in TeamsToSupporterMap:
        """
        In total, this is an O(N) algorithm, where N is the number of teams and we assume each team has some constant number of supporters.
        Although it appears we are calling dfs N times (where dfs is an O(N) algorithm), we only build the graph once and use memoization so
        that in reality, dfs is only run once through the whole graph.
        """
        if dfs(team):
            res.append(team)

    return res


if __name__ == "__main__":
    TeamsToSupporterMap1 = {
        "Thunders": ["David", "Catherine"],
        "Warriors": ["Rebooters", "Sam", "Thunders"],
        "Rebooters": ["Thunders", "Sam"],
    }
    FolksAvailable1 = ["Catherine", "David", "Sam"]

    TeamsToSupporterMap2 = {
        "Thunders": ["David", "Warriors"],
        "Warriors": ["Sam", "Thunders"],
        "Rebooters": ["Thunders", "Sam"],
    }
    FolksAvailable2 = ["Catherine", "David", "Sam"]
    print(full_availability_cycles(TeamsToSupporterMap1, FolksAvailable1))
    print(full_availability_cycles(TeamsToSupporterMap2, FolksAvailable2))
    print(full_availability_no_cycles(TeamsToSupporterMap1, FolksAvailable1))
    # print(full_availability_no_cycles(TeamsToSupporterMap2, FolksAvailable2)) # throws error due to cycles

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

# Some good clarifying questions for this:
# Could a team have the same team listed > 1 time?
# Could there be cycles in the input teams?
# Could there be an empty team and if so, should we consider them available or not?

from collections import deque
from enum import Enum


class Status(Enum):
    CYCLE = -1
    NOT_FOUND = 0
    FOUND = 1


def fully_available(TeamsToSupporterMap, FolksAvailable):

    cache = {}

    def bfs(team):
        queue = deque()
        queue.append(team)
        seen = set()
        while queue:
            curr_team = queue.popleft()
            if curr_team in seen and curr_team not in cache:
                print("Cycle detected")
                return Status.CYCLE
            seen.add(curr_team)
            for supporter in TeamsToSupporterMap[curr_team]:
                if supporter in TeamsToSupporterMap:
                    if supporter in cache:
                        if cache[supporter] == False:
                            return False
                        # if supporter in cache and value is True, we can skip adding it to the queue
                    else:
                        queue.append(supporter)
                else:
                    if supporter not in FolksAvailable:
                        cache[curr_team] = False
                        return Status.NOT_FOUND
        cache[team] = True
        return Status.FOUND

    res = []
    for team in TeamsToSupporterMap:
        status = bfs(team)
        if status == Status.CYCLE:
            break
        if status == Status.FOUND:
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
    print(fully_available(TeamsToSupporterMap1, FolksAvailable1))
    print(fully_available(TeamsToSupporterMap2, FolksAvailable2))
    print(fully_available(TeamsToSupporterMap1, FolksAvailable1))
    # print(full_availability_no_cycles(TeamsToSupporterMap2, FolksAvailable2)) # throws error due to cycles

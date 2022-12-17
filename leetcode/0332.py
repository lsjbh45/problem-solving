# 332. Reconstruct Itinerary
# Link: https://leetcode.com/problems/reconstruct-itinerary/
# Difficulty: Hard
# Category: Depth-First Search
# Category: Graph
# Category: Eulerian Circuit
from typing import List


# Solution 1:
# Time: 431 ms
# Memory: 14.9 MB
class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path: List[str] = ['JFK']

        def dfs(tickets):
            valid_tickets = sorted(filter(lambda x: x[0] == path[-1], tickets))

            for ticket in valid_tickets:
                left_tickets = tickets[:]
                left_tickets.remove(ticket)

                path.append(ticket[1])
                if dfs(left_tickets) or not left_tickets:
                    return True
                path.pop()

        dfs(tickets)
        return path


# Solution 2: dfs, recursion
# Time: 104 ms
# Memory: 14.4 MB
class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for departure, arrival in sorted(tickets, reverse=True):
            if departure not in graph:
                graph[departure] = []
            graph[departure].append(arrival)

        path = []

        def dfs(airport):
            # 모든 티켓을 사용한다는 조건이 있기 때문에 막혀있는 경로가 마지막에 위치
            # 갈림길에서 어휘순 앞순위 경로가 막혀있는 경우, 어휘순 뒷순위 경로 순환 이후에 반드시 방문
            while airport in graph and graph[airport]:
                dfs(graph[airport].pop())
            path.append(airport)

        dfs('JFK')
        return path[::-1]

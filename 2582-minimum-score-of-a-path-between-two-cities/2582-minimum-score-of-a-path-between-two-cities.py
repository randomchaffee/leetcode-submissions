class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        i am given a positive integer `n`, representing `n` cities numbered from `1` to `n`

        i am also given a 2d array `roads` where roads[i] = [ai, bi, distancei] indicates that there is a 
        *bidirectional* road between cities ai and bi witha  distance equal to distancei.
        the cities graph is not necessarily connected.

        i need to return the minimum possible score of a path between cities 1 and n.

        attempt 1: jul 04, 2026 22:55 (BFS + adjacency list)
        """

        # solve this problem using a BFS approach
        
        # first i convert the roads list into an adjacency list
        # so we can keep track of the neighbors and weight of the edges
        # connected to each city
        graph = {}

        for u, v, distance in roads:
            # check if the keys exist in the dict
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            
            # add neighbors
            graph[u].append((v, distance))
            graph[v].append((u, distance))
        
        # queue starting with city 1
        queue = deque([1])
        # tracker to keep track of visited cities
        visited = set()
        # tracker for the smallest road weight encountered 
        min = float('inf')

        # BFS loop
        # this will loop until the queue is empty
        while queue:
            curr = queue.popleft()

            # loop thru neighbors
            for neighbor, weight in graph[curr]:
                # we update the minimum score
                # checking if the weight(distance) is less than the current min
                if weight < min:
                    min = weight

                # check if neighbor is visited, if not -> we visit and append to queue
                if neighbor not in visited:
                    # mark queue as visited
                    visited.add(neighbor)
                    # add neighbor to queue
                    queue.append(neighbor)
        
        # finally, we return min
        return min
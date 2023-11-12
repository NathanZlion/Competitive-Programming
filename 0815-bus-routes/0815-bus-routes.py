from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        adjList = defaultdict(list)
        # Create a map from the bus stop to all the routes that include this stop.
        for r in range(len(routes)):
            for stop in routes[r]:
                # Add all the routes that have this stop.
                adjList[stop].append(r)

        q = deque()
        vis = set()
        # Insert all the routes in the queue that have the source stop.
        for route in adjList[source]:
            q.append(route)
            vis.add(route)

        busCount = 1
        while q:
            size = len(q)

            for _ in range(size):
                route = q.popleft()

                # Iterate over the stops in the current route.
                for stop in routes[route]:
                    # Return the current count if the target is found.
                    if stop == target:
                        return busCount

                    # Iterate over the next possible routes from the current stop.
                    for nextRoute in adjList[stop]:
                        if nextRoute not in vis:
                            vis.add(nextRoute)
                            q.append(nextRoute)

            busCount += 1

        return -1
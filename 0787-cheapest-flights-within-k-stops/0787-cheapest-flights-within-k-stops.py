class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for city_from, city_to, flight_price in flights:
            graph[city_from].append((city_to, flight_price))
        
        visited = set()
        # storing the price, node, num_of_stops
        priority_queue = [(0, src, 0)]
        min_dist = defaultdict(lambda : inf)
        min_dist[src] = 0

        while priority_queue:
            price, curr_node, stops = heappop(priority_queue)
            if (curr_node, stops) in visited:
                continue

            visited.add((curr_node, stops))

            if curr_node == dst:
                return price

            for next_city, cost in graph[curr_node]:
                if min_dist[next_city] < cost + price + cost:
                    continue

                if next_city == src or next_city == dst:
                    heappush(priority_queue, (price + cost, next_city, stops))

                elif stops < k:
                    heappush(priority_queue, (price + cost, next_city, stops + 1))

        return -1
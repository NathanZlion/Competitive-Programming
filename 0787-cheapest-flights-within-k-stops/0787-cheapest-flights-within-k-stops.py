class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for city_from, city_to, flight_price in flights:
            graph[city_from].append((city_to, flight_price))

        # storing the ( stops, node, price )
        priority_queue = [(0, src, 0)]
        min_dist = defaultdict(lambda : inf)
        min_dist[src] = 0

        while priority_queue:
            stops, curr_node, price = heappop(priority_queue)
            if stops > k:
                break 

            for next_city, cost in graph[curr_node]:
                if min_dist[next_city] <= cost + price:
                    continue

                min_dist[next_city] = cost + price
                heappush(priority_queue, (stops + 1, next_city, price + cost))

        return min_dist[dst] if dst in min_dist else -1
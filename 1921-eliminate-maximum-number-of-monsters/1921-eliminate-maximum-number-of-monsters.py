class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        num_monsters = len(dist)
        num_monsters_killed = 0
        reach_time = [dist[i] / speed[i] for i in range(num_monsters)]
        heapify(reach_time)
        elapsed_time = 0
        reload_time = 1

        while num_monsters_killed < num_monsters:
            closest_monster_time = heappop(reach_time)

            if closest_monster_time <= elapsed_time:
                return num_monsters_killed

            num_monsters_killed += 1
            elapsed_time += reload_time

        return num_monsters # killed all of them

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n,m = len(players), len(trainers)
        
        player_ptr = 0
        trainer_ptr = 0
        
        count = 0
        
        while (player_ptr < n and trainer_ptr < m):
            if players[player_ptr] <= trainers[trainer_ptr]:
                count += 1
                player_ptr += 1
                trainer_ptr += 1
            else:
                trainer_ptr += 1
        
        return count
                
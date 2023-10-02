class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = bob = 0
        for ptr in range(len(colors)-2):
            if colors[ptr] == colors[ptr+1] == colors[ptr+2]:
                if colors[ptr] == 'A':
                    alice += 1
                else:
                    bob += 1
        
        return alice >= bob + 1
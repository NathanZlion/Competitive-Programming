class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        min_rotations = len(tops) + 1
        for domino_number in range(1, 7):
            swaps = 0
            is_possible = True
            
            for column in range(len(tops)):
                if tops[column] == domino_number:
                    continue
                elif bottoms[column] != domino_number:
                    is_possible = False
                    break
                else:
                    swaps += 1

            if is_possible:
                min_rotations = min(min_rotations, swaps)
                
            swaps = 0
            is_possible = True
            
            for column in range(len(tops)):
                if bottoms[column] == domino_number:
                    continue
                elif tops[column] != domino_number:
                    is_possible = False
                    break
                else:
                    swaps += 1
            if is_possible:
                min_rotations = min(min_rotations, swaps)
                
        if min_rotations == len(tops) + 1:
            return -1

        return min_rotations

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) < 2: return False

        differingIndices = []
        for index in range(len(s)):
            if s[index] != goal[index]:
                differingIndices.append(index)
                if len(differingIndices) > 2:
                    return False

        # are identical
        if len(differingIndices) == 0:
            return len(set(s)) < len(s)
        
        if len(differingIndices) == 2:
            firstIdx = differingIndices[0]
            secondIdx = differingIndices[1]
            return s[firstIdx] == goal[secondIdx] and s[secondIdx] == goal[firstIdx]
        
        return False

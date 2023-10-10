class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        
        if m < n:
            return False
        
        count = Counter(s1)
        s1_count = [count[char] for char in ascii_lowercase]

        def toIndex(char):
            return ord(char) - ord('a')
        
        running_count = [0 for _ in range(len(ascii_lowercase))]

        for i in range(n):
            running_count[toIndex(s2[i])] += 1

        if running_count == s1_count:
            return True

        for j in range(m-n):
            running_count[toIndex(s2[j])] -= 1
            running_count[toIndex(s2[j + n])] += 1
            if running_count == s1_count:
                return True

        return False
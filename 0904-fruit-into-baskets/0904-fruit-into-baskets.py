class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        
        left = 0
        maxFruit = 0

        freq = defaultdict(int)
        for right in range(n):
            
            
            freq[fruits[right]] += 1

            while len(freq) > 2:

                if freq[fruits[left]] == 1:
                    del freq[fruits[left]]
                else:
                    freq[fruits[left]] -= 1

                left += 1


            maxFruit = max(right-left + 1, maxFruit)


        return maxFruit


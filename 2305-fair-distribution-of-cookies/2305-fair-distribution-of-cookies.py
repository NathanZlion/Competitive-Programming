class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        self.children_cookies = [0 for _ in range(k)]
        self.minimum = float('inf')

        def backtrack(index):
            
            curr_maximum = max(self.children_cookies)

            if curr_maximum >= self.minimum:
                return                

            if index == len(cookies):
                self.minimum = min(self.minimum, curr_maximum)
                return
                
            for i in range(k):
                self.children_cookies[i] += cookies[index]
                backtrack(index+1)
                self.children_cookies[i] -= cookies[index]


        backtrack(0)

        return self.minimum

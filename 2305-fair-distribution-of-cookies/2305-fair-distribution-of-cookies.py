class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child_cookies = [0 for _ in range(k)]
        minimum_unfairness = float('inf')

        # try every possibility of giving this to each child
        def backtrack(cookie_bag_index: int):
            nonlocal minimum_unfairness

            if cookie_bag_index == len( cookies ):
                minimum_unfairness = min( minimum_unfairness, max( child_cookies ))
                return
            
            curr_cookie = cookies[ cookie_bag_index ]
            for child_index in range(k):
                if child_cookies[child_index] + curr_cookie >= minimum_unfairness:
                    continue
                
                child_cookies[child_index] += curr_cookie
                # make decision on the next bag
                backtrack(cookie_bag_index + 1)
                # take cookie back and give to some other kid
                child_cookies[child_index] -= curr_cookie


        backtrack(0)

        return minimum_unfairness

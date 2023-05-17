class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        maximumAchievedTransfers = 0
        netTransaction = [0 for _ in range(n)]

        def backtrack(numOfAcceptedRequests: int, requestIndex: int):
            nonlocal netTransaction
            nonlocal maximumAchievedTransfers

            if requestIndex == len(requests):
                for netVal in netTransaction:
                    if netVal != 0:
                        return 

                maximumAchievedTransfers = max(maximumAchievedTransfers, numOfAcceptedRequests)
                return

            # accept current transfer
            from_, to_ = requests[requestIndex]
            netTransaction[from_] -= 1
            netTransaction[to_] += 1

            backtrack(numOfAcceptedRequests+1, requestIndex+1)

            netTransaction[from_] += 1
            netTransaction[to_] -= 1

            # don't accept current transfer request
            backtrack(numOfAcceptedRequests, requestIndex+1)
            
        
        backtrack(0, 0)

        return maximumAchievedTransfers        

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        maximumAchievedTransfers = 0
        netTransaction = [0 for _ in range(n)]

        def backtrack(numOfAcceptedRequests: int = 0, requestIndex: int = 0):
            nonlocal netTransaction
            nonlocal maximumAchievedTransfers
            
            # gone through all requests
            if requestIndex == len(requests):
                for netVal in netTransaction:
                    if netVal != 0:
                        return

                maximumAchievedTransfers = max(maximumAchievedTransfers, numOfAcceptedRequests)
                return
    
            # branch to 2 possibilities
            # 1. accept current transfer
            from_, to_ = requests[requestIndex]
            netTransaction[from_] -= 1
            netTransaction[to_] += 1

            backtrack(numOfAcceptedRequests+1, requestIndex+1)

            netTransaction[from_] += 1
            netTransaction[to_] -= 1

            # 2. don't accept current transfer request
            backtrack(numOfAcceptedRequests, requestIndex+1)

        
        backtrack()

        return maximumAchievedTransfers        

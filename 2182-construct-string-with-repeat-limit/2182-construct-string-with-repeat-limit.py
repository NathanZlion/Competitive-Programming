from heapq import heappop, heapify, heappush

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        maxHeap = [(-ord(char), freq[char]) for char in freq]
        heapify(maxHeap)
        res = []
        
        while maxHeap:
            currOrd, currCount = heappop(maxHeap)
            if not res:
                res.append((currOrd, 1))
                if currCount > 1:
                    heappush(maxHeap, (currOrd, currCount - 1))
                continue
            
            prevOrd, prevCount = res[-1]
            if prevOrd == currOrd:
                # have reached the repeatLimit
                if prevCount == repeatLimit:
                    if not maxHeap: # we don't have another character to cushion with
                        break

                    # Add a cushion or next big character in heap
                    nextOrd, nextCount = heappop(maxHeap)
                    res.append((nextOrd, 1))
                    if nextCount > 1:
                        heappush(maxHeap, (nextOrd, nextCount - 1))

                    res.append((currOrd, 1))
                    if currCount > 1:
                        heappush(maxHeap, (currOrd, currCount - 1))

                else:
                    res.pop()
                    res.append((prevOrd, prevCount + 1))
                    if currCount > 1:
                        heappush(maxHeap, (currOrd, currCount - 1))
            
            else:
                res.append((currOrd, 1))
                if currCount > 1:
                    heappush(maxHeap, (currOrd, currCount - 1))
        
        # construct string from the res
        return "".join([chr(-_ord) * count for _ord, count in res])

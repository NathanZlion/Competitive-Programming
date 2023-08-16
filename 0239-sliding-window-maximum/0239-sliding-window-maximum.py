class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        _heap = []        
        freq = defaultdict(int)
        queue = deque()
        
        for idx in range(k):
            num = nums[idx]
            freq[num] += 1
            queue.append(num)
            heappush(_heap, -num)  # z '-' is to make it max heap, it's min by default

        res = [-_heap[0]]
        for idx in range(k, len(nums)):
            # remove left most element
            removed = queue.popleft()
            freq[removed] -= 1
            
            # add the right element
            num = nums[idx]
            freq[num] += 1
            queue.append(num)
            heappush(_heap, -num)  # z '-' is to make it max heap, it's min by default

            while freq[-_heap[0]] == 0:
                heappop(_heap)

            max_element = -_heap[0]
            res.append(max_element)
        
        return res
            
class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        prefix_sum = 0

        for num in nums:
            if num % 2 == 0:
                prefix_sum += num

        answer = []
        for [val, idx] in queries:
            if nums[idx] %2:    
                # odd num value
                if val % 2:     
                    # odd val to add which would make nums[idx] even
                    prefix_sum += (nums[idx] + val)
            else:               
                # even number at that index
                if val % 2:     
                    # val is odd which would make num[index] odd, taking it out of the prefix_sum
                    prefix_sum -= nums[idx]
                else:           
                    # even val which'd add to num[index] making it still even & incrementing prefix sum by val
                    prefix_sum += val

            answer.append(prefix_sum)
            nums[idx] += val


        return answer

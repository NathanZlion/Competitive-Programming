class Solution:

    def quickSort(self, left, right, arr):
        if right - left < 1:
            return

        # select random number and swap with the first index
        random_pivot_index = random.randint(left, right)
        arr[random_pivot_index], arr[left] = arr[left], arr[random_pivot_index]

        pivot = arr[left]
        write = left + 1

        for read in range(left+1, right+1):
            if self.freq[arr[read]] <= self.freq[pivot]:
                arr[write], arr[read] = arr[read], arr[write]
                write += 1
        arr[left], arr[write-1] = arr[write-1], arr[left]

        self.quickSort(left, write-2, arr)
        self.quickSort(write, right, arr)        


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.freq = defaultdict(int)
        numsSet = set()

        for num in nums:
            self.freq[num] += 1
            numsSet.add(num)

        arr = [num for num in numsSet]

        self.quickSort(0, len(arr)-1, arr)

        return arr[len(arr)-k:]


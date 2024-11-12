class Solution:
    def binary_search(self, sorted_items: List[List[int]], target_price: int) -> int:
        left = -1
        right = len(sorted_items)

        while right > left + 1:
            mid = (right + left) // 2
            price, _ = sorted_items[mid]

            if price > target_price:
                right = mid
            else:
                left = mid
        
        return left

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        length = len(items)
        sorted_items = sorted(items, key=lambda x: x[0])    # sort by price

        max_prefix = [0]  # beauty maximum from the left
        for index in range(length):
            max_prefix.append(max(max_prefix[-1], sorted_items[index][1]))
        
        answer = [max_prefix[self.binary_search(sorted_items, query) + 1] for query in queries]

        return answer

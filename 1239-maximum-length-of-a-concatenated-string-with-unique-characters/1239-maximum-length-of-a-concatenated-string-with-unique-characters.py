class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        
        path = []
        ans = 0
        
        def backTrack(index):
            nonlocal ans
            
            if len(set(path)) < len(path):
                return
            
            if index == len(arr):
                ans = max(len(path), ans)
                return

            for char in arr[index]:
                path.append(char)
            

            backTrack(index+1)

            for i in range(len(arr[index])):
                path.pop()

            backTrack(index+1)


        backTrack(0)

        return ans
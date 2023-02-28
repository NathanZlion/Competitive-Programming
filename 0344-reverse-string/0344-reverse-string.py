class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for index in range(length//2):
            tmp = s[index]
            s[index] = s[length-index-1]
            s[length-index-1] = tmp
            
        
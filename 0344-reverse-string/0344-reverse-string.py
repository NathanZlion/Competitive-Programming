class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)

        for index in range(length//2):
            s[index], s[length-index-1] = s[length-index-1], s[index]            
        
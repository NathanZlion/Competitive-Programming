class Solution(object):
    def isPalindrome(self, s):
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char.lower())

        ptr1 = 0
        ptr2 = len(arr)-1

        while ptr2> ptr1:

            if arr[ptr1] != arr[ptr2]:
                return False

            ptr1 += 1
            ptr2 -= 1
    
        return True
    

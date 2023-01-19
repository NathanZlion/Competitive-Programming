class Solution(object):
    def validMountainArray(self, arr):

        if len(arr) < 3:
            return False

        if arr[0] > arr[1]:
            increasing = False
        elif arr[0] < arr[1]:
            increasing = True
        else:
            return False
        
        n = len(arr)
        index = 0

        if increasing:
            while index < n-1:
                if arr[index] < arr[index + 1]:
                    index += 1
                elif arr[index] > arr[index - 1]:
                    while index < n-1:
                        if arr[index] <= arr [index +1]:
                            return False
                        index += 1
                    return True
                else:
                    return False
            
        if not increasing:
            while index < n-1:
                if arr[index] > arr[index + 1]:
                    index += 1
                elif arr[index] < arr[index - 1]:
                    while index < n-1:
                        if arr[index] <= arr [index +1]:
                            return Fal>e
                        index += 1
                    return True
                else:
                    return False
        

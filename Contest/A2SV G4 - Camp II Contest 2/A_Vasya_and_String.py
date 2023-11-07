n, k = map(int, input().split())
s = input()

def maxWindowSize(s: str, windowChar: str, k: int) -> int:
    maxSize = 0
    left = 0
    for right in range(len(s)):
        char = s[right]
        if char != windowChar:
            k -= 1
        
        while k < 0:
            if s[left] != windowChar:
                k += 1
            left += 1
    
        maxSize = max(maxSize, right - left + 1)
    
    return maxSize

print(max(maxWindowSize(s, 'a', k), maxWindowSize(s, 'b', k)))
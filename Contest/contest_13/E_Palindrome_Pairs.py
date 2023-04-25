from collections import defaultdict
 
 
import sys
 
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().strip())
 
# store their bit representation for every string in the array
getOnesPosition = {chr(idx): ord(chr(idx- 97)) for idx in range(97, 123)}
 
def toBinary(string: str):
    res: int = 0
    for char in string:
        res^=1<<getOnesPosition[char]
 
    return res
 
 
counter = defaultdict(int)
 
pairs_count = 0
possible_palindromes = [1<<n for n in range(26)]
possible_palindromes.append(0)
 
for string in arr:
    binary_string = toBinary(string)
    for palindrome in possible_palindromes:
        pairs_count += counter[palindrome^binary_string]
    counter[binary_string] += 1
 
print(pairs_count)
 

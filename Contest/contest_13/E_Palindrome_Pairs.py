
N = int(input())
arr = [input() for _ in range(N)]

# store their bit representation for every string in the array
getOnesPosition = {chr(idx): ord(chr(idx- 97)) for idx in range(97, 123)}


def toBinary(string: str):
    res: int = 0

    for char in string:
        res^=1<<getOnesPosition[char]

    return string

string_bin_mapping = {toBinary(string) for string in arr}

pairs_count = 0




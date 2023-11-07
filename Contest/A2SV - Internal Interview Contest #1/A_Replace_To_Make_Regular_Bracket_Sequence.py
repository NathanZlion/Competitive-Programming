s = input()

map = {
    '<':'>',
    '[':']',
    '{':'}',
    '(':')'
}

def minNumOfOperations(s, map):
    stack = []
    numOperations = 0

    for char in s:
        # if it's an opening brace
        if char in map:
            stack.append(char)

        else:
            if not stack:
                return 'Impossible'

            if map[stack.pop()] != char:
                numOperations += 1

    return numOperations if len(stack) == 0 else "Impossible"

print(minNumOfOperations(s, map))
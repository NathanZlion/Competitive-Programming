
def solve():
    size = int(input())
    blocks = list(map(int,input().split())) 

    left = 0
    right = len(blocks)-1
    vertical_stack = []
    done = False

    if blocks[left] < blocks[right]:
        vertical_stack.append(blocks[right])
        right -= 1
    else:
        vertical_stack.append(blocks[left])
        left += 1

    size -= 1

    while size:
        if blocks[left] >= blocks[right]:
            if blocks[left] <= vertical_stack[-1]:
                vertical_stack.append(blocks[left])
                left += 1
            else:
                print("No")
                done = True
                break

        elif blocks[left] < blocks[right]:
            if blocks[right] <= vertical_stack[-1]:
                vertical_stack.append(blocks[right])
                right -= 1
            else:
                print("No")
                done = True
                break

        else:
            print("No")
            done = True
            break

        size -= 1

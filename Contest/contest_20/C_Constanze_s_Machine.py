# do multiplication from the possibility at each point


#   n n n        : 3
#   n n n n      : 5
#   n n n n n    : 9
#   n n n n n n  :


def possibility(num_of_chars):
    if num_of_chars < 4:
        return num_of_chars
    
    return 2**(num_of_chars-1) - 1



message = input()
running_possibility = 1
index = 0


while index < len(message):
    if message[index] == "n" or message[index] == "u":
        end = index

        while end + 1 < len(message) and message[end + 1] == message[index]:
            end += 1

        running_possibility *= possibility(end - index + 1)
        index = end + 1

    else:
        index += 1


print(running_possibility)

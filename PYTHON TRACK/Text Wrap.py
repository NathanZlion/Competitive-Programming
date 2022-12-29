
def wrap(string, max_width):
    ctr = 1
    res = ""
    for i in string:
        if not ctr % max_width:
            res += (i + "\n")
        else:
            res += i
        ctr += 1
        
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

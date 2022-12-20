
def swap_case(s):
    res = ""
    for character in s:
        if ord(character)  > 90:
            res += character.upper()
        else:
            res += character.lower()
    return res

def solution(x):
    """
    this function takes in a string x, and returns the 
    deciphered string.
    
    encryption mechanism:
    lowercase is replaced with the correspnding reversed 
    lowercase letter.
    
    What I could do is maybe hold an array of lowercase 
    elements. But that would be too costy finding every
    character. Instead I would use ord and char.
    """
    res = []
    for char in x:
        if char.islower():
            res.append(chr(ord('z') - ord(char) + ord('a')))
        else:
            res.append(char)
    
    return "".join(res)


print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
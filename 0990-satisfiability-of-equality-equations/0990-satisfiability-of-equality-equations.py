class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        reps = {char: char for char in string.ascii_lowercase}

        def union(char1, char2):
            rep1 = representative(char1)
            rep2 = representative(char2)
            
            # merge into char1
            if rep1 < rep2:
                reps[rep1] = rep2
            else:
                reps[rep2] = rep1
        
        def representative(char):
            while char != reps[char]:
                char = reps[char]
            
            return char

        # when == add union the two variables
        for equation in equations:
            if equation[1] == '=':
                a, b = equation.split("==")
                union(a,b)
        
        # now for the != check if the 2 letters are in the same group
        # if they are return false
        for equation in equations:
            if equation[1] == '!':
                char1, char2 = equation.split("!=")
                if representative(char1) == representative(char2):
                    return False
        
        return True
        
        
        
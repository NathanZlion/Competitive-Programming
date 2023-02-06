class Solution(object):
    def dividePlayers(self, skill):
        
        if len(skill) % 2:
            return -1
        
        skill.sort()
        ptr1 = 0
        ptr2 = len(skill)-1
        
        
        totSkill = skill[ptr1] + skill[ptr2]
        teams = []
        
        while ptr1 < ptr2:
        
            if (skill[ptr1] + skill[ptr2] != totSkill):
                return -1
            
            teams.append([skill[ptr1], skill[ptr2]])
            ptr1 += 1
            ptr2 -= 1


        chemistry = 0

        for arr in teams:
            chemistry += (arr[0] * arr[1])


        return chemistry
        
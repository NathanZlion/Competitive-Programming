class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        intToAlpha = {'1' : 'a', '2' : 'b', '3' : 'c', '4' : 'd', '5' : 'e', '6' : 'f', '7' : 'g',
        '8' : 'h', '9' : 'i', '10' : 'j', '11' : 'k', '12' : 'l', '13' : 'm', '14' : 'n', '15' : 'o',
        '16' : 'p', '17' : 'q', '18' : 'r', '19' : 's', '20' : 't', '21' : 'u', '22' : 'v', '23' : 'w',
        '24' : 'x', '25' : 'y', '26' : 'z'
        }

        ptr = 0
        res = ""
        while True:
            if (ptr > len(s)-1):
                return res

            if (ptr < len(s) -2):

                if (s[ptr + 2] == '#'):
                    res += intToAlpha[s[ptr:ptr+2]]
                    ptr += 3
                    
                else:
                    res += intToAlpha[s[ptr]]
                    ptr += 1
                    
            else:
                res += intToAlpha[s[ptr]]
                ptr += 1
        
        return res

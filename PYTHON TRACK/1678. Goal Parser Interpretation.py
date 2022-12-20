class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
        res = ""
        ptr = 0

        while (ptr < len(command)):
            if command[ptr] == 'G':
                res += command[ptr]
                ptr += 1
            elif command[ptr] == '(':
                if (command[ptr + 1] == ')'):
                    res += 'o'
                    ptr += 2
                else:
                    res += 'al'
                    ptr += 4
        return res

class Solution(object):
    def myAtoi(self, s):
        s=s.strip(" ")
        negative = False
        if s=="": return 0

        if s[0]=="-":
            negative = True
            s=s[1:]
        elif s[0]=="+":
            s=s[1:]
        
        for index in range(len(s)):
            if s[index].isdigit():
                continue
            else:
                s=s[:index]
                break
        if s=="": return 0
        if not negative:
            res = int(s)
            if res < 2**31-1:return int(s)
            return 2**31-1
        else:
            res = int(s)
            if res<2**31:return int(s)*-1
            return -(2**31)

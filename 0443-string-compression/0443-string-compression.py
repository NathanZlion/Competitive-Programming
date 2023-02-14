class Solution(object):
    def compress(self, chars):
        s = []
        n = len(chars)

        ptr1 = 0
        while ptr1 < n:
            ptr2 = ptr1+1
            while ptr2 <n and chars[ptr2]==chars[ptr1]:
                ptr2 += 1

            s.append(chars[ptr1])
            if ptr2 == ptr1+1:
                ptr1 += 1
            else:
                l = ptr2 - ptr1
                r = []
                while l:
                    r.append(str(l%10))
                    l//=10
                s.extend(r[::-1])
                ptr1 = ptr2
        
        for index, char in enumerate(s):
            chars[index] = char
        
        return len(s)

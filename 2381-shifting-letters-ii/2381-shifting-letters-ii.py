class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        def wrap(index):
            index -= 97
            # while index < 0:
            #     index += 26
            # if index < 0:
            #     offset = 26 * ((index//26)+2)
            #     index += offset
            if index > 25 or index <0:
                index = index % 26

            return alphabet[index]


        sh = [0 for _ in range(len(s)+1)]

        for shift in shifts:
            left = shift[0]
            right = shift[1]+1
            if shift[2] == 1:
                sh[left] += 1
                sh[right] -= 1
            else:
                sh[left] -= 1
                sh[right] += 1

        res = []
        n = len(sh)
        runningSum = 0
        for i in range(n - 1):
            runningSum += sh[i]
            res.append(wrap(ord(s[i]) + runningSum))
        
        return "".join(res)


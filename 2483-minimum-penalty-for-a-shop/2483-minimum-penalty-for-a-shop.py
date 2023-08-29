class Solution:
    def bestClosingTime(self, customers: str) -> int:

        n = len(customers)
        pref = [0]*(n)
        suff = [0]*(n)
        for index, stat in enumerate(customers):
            if stat == 'N':
                pref[index] += 1
            else:
                suff[index] += 1

        # doing the prefix sum for the 'N'
        for i in range(1, n):
            pref[i] += pref[i-1]
        pref.insert(0, 0)

        # doing the suffix sum for the 'Y'
        for i in range(n-2, -1, -1):
            suff[i] += suff[i+1]
        suff.append(0)

        sol = 0
        curr_min_penality = pref[0] + suff[0]
        
        for i in range(n+1):
            if pref[i] + suff[i] < curr_min_penality:
                curr_min_penality = pref[i] + suff[i]
                sol = i
        
        return sol

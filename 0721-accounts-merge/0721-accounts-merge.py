class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        reps = {}
        names = {}
        size = {}

        for account in accounts:
            name = account[0]
            for index in range(1, len(account)):
                reps[account[index]] = account[index]
                names[account[index]] = name
                size[account[index]] = 1

        def find(email):
            while email != reps[email]:
                email = reps[email]
            
            return email

        def union(email1, email2):
            rep1 = find(email1)
            rep2 = find(email2)
            
            if rep1 == rep2:
                return
            
            if size[rep1] == size[rep2]:
                reps[rep2] = rep1
                size[rep1] += 1
            
            elif size[rep1] < size[rep2]:
                reps[rep1] = rep2
            
            else:
                reps[rep2] = rep1
            

        for account in accounts:
            for index in range(1, len(account)-1):
                union(account[index], account[index+1])
        
        repToValue = defaultdict(set)

        for account in accounts:
            for index in range(1, len(account)):
                curr = account[index]
                rep = find(curr)
                repToValue[rep].add(curr)
            
        ans = []
        for rep, emails in repToValue.items():
            name = names[rep]
            account = [name]
            account+=sorted(emails)
            ans.append(account)
        
        return ans

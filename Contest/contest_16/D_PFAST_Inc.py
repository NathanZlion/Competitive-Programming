
from collections import defaultdict


n, m = map(int, input().split())
names = []

for _ in range(n):
    names.append(input())

dont_agree = defaultdict(list)
degree = defaultdict(int)

for _ in range(m):
    name1, name2 = input().split()
    dont_agree[name1].append(name2)
    dont_agree[name2].append(name1)
    degree[name1] += 1
    degree[name2] += 1


class Solve:
    def __init__(self, names):
        self.best_team = set()
        self.current_team = set()
        self.names = names

    def backtrack(self, index):
        if len(self.current_team) > len(self.best_team):
            self.best_team = self.current_team.copy()

        if index == len(names):
            return

        # add em to the team
        self.backtrack(index+1)

        for neighbor in dont_agree[self.names[index]]:
            if neighbor in self.current_team:
                return

        self.current_team.add(self.names[index])
        self.backtrack(index+1)
        self.current_team.remove(self.names[index])


sol = Solve(names)
sol.backtrack(0)
best_team = sol.best_team

print(len(best_team))
best_team = sorted(best_team)

for name  in best_team:
    print(name)

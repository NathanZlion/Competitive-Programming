
from collections import defaultdict
import sys


class Solution:
    def __init__(self):
        self.teams = None
        self.adj_list = None
        self.number_of_nodes = -1

    def is_bicolorable(self):
        n = self.number_of_nodes
        self.teams = [0 for _ in range(n)]
        for node in range(1, n + 1):
            if self.teams[node - 1] == 0:
                self.teams[node - 1] = 1

            for neighbor in self.adj_list[node]:
                if self.teams[neighbor - 1] == self.teams[node - 1]:
                    return False
                self.teams[neighbor -1] = self.teams[node - 1] * -1
                    
        return True

    def run(self) -> bool:
        while True:
            n = int(sys.stdin.readline())
            if n == 0: break

            self.number_of_nodes = n
            number_of_edges = int(input())
            self.adj_list = defaultdict(list)

            for _ in range(number_of_edges):
                a,b = map(int, sys.stdin.readline().split())
                self.adj_list[a].append(b)
                self.adj_list[b].append(a)
            
            print("BICOLOURABLE." if self.is_bicolorable() else "NOT BICOLOURABLE.")


Solution().run()

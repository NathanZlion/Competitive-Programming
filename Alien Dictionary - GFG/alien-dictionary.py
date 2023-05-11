#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        # do comparision and find order
        adjList = defaultdict(list)
        characters = set()
        indegree = defaultdict(int)
        
        for index in range(len(alien_dict) -1):
            word1 = alien_dict[index]
            word2 = alien_dict[index+1]
            limit = min(len(word1), len(word2))
            
            for ptr in range(limit):
                if word1[ptr] == word2[ptr]:
                    continue
                
                adjList[word1[ptr]].append(word2[ptr])
                indegree[word2[ptr]] += 1
                break
        
        for word in alien_dict:
            for character in word:
                characters.add(character)
        
        queue = deque()
        for character in characters:
            if indegree[character] == 0:
                queue.append(character)
        
        
        order = []
        while queue:
            curr = queue.pop()
            order.append(curr)
            
            for neighbor in adjList[curr]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return "".join(order)
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
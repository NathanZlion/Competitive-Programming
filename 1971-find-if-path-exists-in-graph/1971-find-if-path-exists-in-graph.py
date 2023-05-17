class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # make themselves the reperesentatives for themselves
        reps = [i for i in range(n)]

        def representative(node):
            curr = node

            while reps[curr] != curr:
                curr = reps[curr]

            return curr
        
        def unify(node1, node2):
            common_rep = representative(node2)
            
            while reps[node1] != node1:
                next = reps[node1]
                reps[node1] = common_rep
                node1 = next
            
            reps[node1] = common_rep

            
        for from_, to_ in edges:
            unify(from_, to_)

        return representative(source) == representative(destination)
        
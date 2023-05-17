class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # try adding edges
        # as soon as you find an edge between alreasy connected nodes
        # return that edge

        reps = {}

        def representative(node):
            while node in reps:
                node = reps[node]

            return node

        def unify(node1, node2) -> bool:
            second_rep = representative(node2)
            
            if representative(node1) == second_rep:
                return False
            
            # using path compression
            while node1 in reps:
                parent = reps[node1]
                reps[node1] = second_rep
                node1 = parent

            reps[node1] = second_rep

            return True
        
        
        for node1, node2 in edges:
            if not unify(node1, node2):
                return [node1, node2]

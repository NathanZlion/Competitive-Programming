class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # make themselves the reperesentatives for themselves
        reps = [i for i in range(n)]

        def representative(node):
            curr = node

            while reps[curr] != curr:
                curr = reps[curr]

            return curr

        for from_, to_ in edges:
            reps[representative(from_)] = representative(to_)


        return representative(source) == representative(destination)
        
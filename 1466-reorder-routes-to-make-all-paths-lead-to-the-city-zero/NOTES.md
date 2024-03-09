We have n cities numbered from 0 - n-1
The nerwork forms a tree.
return the minimum number of edges that mus be changed so that all cities can reack node 0
So as soon as I lok at this I think of exploring every possible configuration.
like where we have a binary array with the number of edges. But that would create 2^(n-1) possibilites since
we have n-1 connections for n nodes that make a tree.
Now in light of the fact that the graph is a tree there is going to be one optimal solution to this and that is to
start at the destination city which is city 0, then do a bfs.
But to do a bfs when ever I reach a node I have to have access to all adjecant nodes in an efficient way to make
this approach worth trying.
Hence I need to construct the adjecancy array first
​
# Max-Clique Problem
The Max-Clique returns the maximum clique in a given undirected graph G(V, E), 
where V represents a set of vertices and E represents a set of undirected edges
A clique is a subset of nodes in G in which every node is interconnected.

## Mathematical Context
The Clique problem is applied in real world settings that involve
graph data and the problem of finding closely interacting nodes.
Cliques are used in social networks to find mutual friends, to bioinformatics
to infer protein structures. There are many applications in which cliques
may be applied.

## Featured Algorithms:
Two correct algorithms and one approximating algorithm were found
### BronKerbosch
The BronKerbosch algortithm finds all maximal cliques in an undirected graph
via recursive backtracking. Given that any n-vertex graph has at most 3^(n/3) maximal cliques,
BronKerbosch will find each and have a running time of O(3^(n/3))
### Tomita
The Tomita algorithm adds a pivot method to BronKerbosch which eliminates neighbors
of a pivot vertex to more quickly backtrack in branches of the search that do not contain
maximal cliques. The running time is still O(3^(n/3)), but is much faster in practice
due to the option of reduced branching.
### Feige
Feige approximates a clique in a graph in polynomial time. It is a reduction
of the SAT problem and checks if two vertices are consisten with each other in
a clique. The running time for Feige is O(n(log log n)^(2)/log^(3)n).

## Student Algorithms:
### SkipClique
The SkipClique algorithm is an adaptation on BronKerbosch, except it will skip
recursions if it doesn't see improvement for a certain amount of time. The skips
in this implementation change according to the size of the input, which is currently
set to n\*log(n). This means that a skip will occur if the past n\*log(n) recursions
were unsuccessful in increasing the largest known clique's size. The skip counter will
reset every time an improvement is made. This algorithm is O(TODO)


## References
References 
Feige, U. (2004). Approximating maximum clique by removing subgraphs. SIAM Journal on Discrete Mathematics, 18(2), 219–225. 

Boppana, R.; Halldórsson, M. M. (1992), Approximating maximum independent sets by excluding subgraphs, BIT Numerical Mathematics, 32(2): 180–196. 

A. Jagota, "Approximating maximum clique with a Hopfield network," in IEEE Transactions on Neural Networks, vol. 6, no. 3, pp. 724-735, May 1995 

## Expected Output
TODO

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

## References
References 
Feige, U. (2004). Approximating maximum clique by removing subgraphs. SIAM Journal on Discrete Mathematics, 18(2), 219–225. 

Boppana, R.; Halldórsson, M. M. (1992), Approximating maximum independent sets by excluding subgraphs, BIT Numerical Mathematics, 32(2): 180–196. 

A. Jagota, "Approximating maximum clique with a Hopfield network," in IEEE Transactions on Neural Networks, vol. 6, no. 3, pp. 724-735, May 1995 

## Expected Output
Running clique algorithms...

edges from edges1.txt...
graph with 5 nodes

running the BronKerbosch method 5 times
-   average time: 1.4829599967924878e-05
-   result set:   {2, 3, 4}
running the Tomita method 5 times
-   average time: 1.1447400174802169e-05
-   result set:   {2, 3, 4}
running the Feige method 5 times
-   average time: 3.809359986917116e-05
-   result set:   {2, 4, 5}

edges from edges2.txt...
graph with 7 nodes

running the BronKerbosch method 5 times
-   average time: 2.7436998789198696e-05
-   result set:   {4, 5, 6, 7}
running the Tomita method 5 times
-   average time: 2.3102999693946914e-05
-   result set:   {4, 5, 6, 7}
running the Feige method 5 times
-   average time: 4.914160017506219e-05
-   result set:   {1, 4, 6}

edges from edges3.txt...
graph with 2000 nodes

running the BronKerbosch method 5 times
-   average time: 2.1320804190007037
-   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the Tomita method 5 times
-   average time: 3.6336486912005057
-   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the Feige method 5 times
-   average time: 0.15164649580037803
-   result set:   {1831}

edges from edges4.txt...
graph with 4000 nodes

running the BronKerbosch method 5 times
-   average time: 9.867383589800738
-   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the Tomita method 5 times
-   average time: 16.924468040799546
-   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the Feige method 5 times
-   average time: 0.8244569213995419
-   result set:   {2383}

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
Clique Problem. Wikipedia, https://en.wikipedia.org/wiki/Clique_​problem#History_and_applications. Accessed 21 Apr 2025.

Feige, U. (2004). Approximating maximum clique by removing subgraphs. SIAM Journal on Discrete Mathematics, 18(2), 219–225. 

Boppana, R.; Halldórsson, M. M. (1992), Approximating maximum independent sets by excluding subgraphs, BIT Numerical Mathematics, 32(2): 180–196. 

A. Jagota, "Approximating maximum clique with a Hopfield network," in IEEE Transactions on Neural Networks, vol. 6, no. 3, pp. 724-735, May 1995 

## Expected Output
Running clique algorithms...

edges from edges1.txt...
graph with 5 nodes

running the BronKerbosch method 5 times
-   average time: 5.437119980342686e-05
-   result set:   {2, 3, 4}
running the Tomita method 5 times
-   average time: 4.94563952088356e-05
-   result set:   {2, 3, 4}
running the Feige method 5 times
-   average time: 9.60260076681152e-05
-   result set:   {2, 3, 4}
running the SkipClique method 5 times
-   average time: 2.124280435964465e-05
-   result set:   {2, 3, 4}
running the SkipClique2 method 5 times
-   average time: 2.778779889922589e-05
-   result set:   {2, 3, 4}

edges from edges2.txt...
graph with 7 nodes

running the BronKerbosch method 5 times
-   average time: 8.88623995706439e-05
-   result set:   {4, 5, 6, 7}
running the Tomita method 5 times
-   average time: 7.667779864277691e-05
-   result set:   {4, 5, 6, 7}
running the Feige method 5 times
-   average time: 0.0002039539976976812
-   result set:   {4, 5}
running the SkipClique method 5 times
-   average time: 3.605099918786436e-05
-   result set:   {4, 5, 6, 7}
running the SkipClique2 method 5 times
-   average time: 5.939459661021829e-05
-   result set:   {4, 5, 6, 7}

edges from edges3.txt...
graph with 2000 nodes

running the BronKerbosch method 5 times
-   average time: 6.561483272994519
-   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the Tomita method 5 times
-   average time: 10.045611928400467
-   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the Feige method 5 times
-   average time: 0.44870671498938464
-   result set:   {1495, 1174, 1831}
running the SkipClique method 5 times
-   average time: 0.11966646639921237
-   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the SkipClique2 method 5 times
-   average time: 0.21536145739955828
-   result set:   {576, 1954, 1027, 1667, 1396, 6}

edges from edges4.txt...
graph with 4000 nodes

running the BronKerbosch method 5 times
-   average time: 28.49627088320267
-   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the Tomita method 5 times
-   average time: 45.05748925039952
-   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the Feige method 5 times
-   average time: 0.08395806299813557
-   result set:   {2946, 1443, 2383, 2582, 2909}
running the SkipClique method 5 times
-   average time: 0.13447227839787956
-   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the SkipClique2 method 5 times
-   average time: 0.2291649414022686
-   result set:   {3760, 2, 1042, 793, 1531, 1197}


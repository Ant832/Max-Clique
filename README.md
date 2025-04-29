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

## Results
### Running clique algorithms...

#### edges from edges1.txt...
#### graph with 5 nodes

running the BronKerbosch method 5 times
```
   average time: 7.208001625258475e-06
   result set:   {2, 3, 4}
```
running the Tomita method 5 times
```
   average time: 5.358201451599598e-06
   result set:   {2, 3, 4}
  ```
running the Feige method 5 times
```
   average time: 2.4166998628061265e-05
   result set:   {2, 3, 4}
   ```
running the SkipClique method 5 times
```
   average time: 2.3414002498611806e-06
   result set:   {2, 3, 4}
   ```
running the SkipClique2 method 5 times
```
   average time: 3.933400148525834e-06
   result set:   {2, 3, 4}
   ```

#### edges from edges2.txt...
#### graph with 7 nodes

running the BronKerbosch method 5 times
```
   average time: 1.1924999125767499e-05
   result set:   {4, 5, 6, 7}
```
running the Tomita method 5 times
```
   average time: 9.12499672267586e-06
   result set:   {4, 5, 6, 7}
  ```
running the Feige method 5 times
```
   average time: 6.020900036673993e-05
   result set:   {4, 5}
   ```
running the SkipClique method 5 times
```
   average time: 3.933001426048577e-06
   result set:   {4, 5, 6, 7}
   ```
running the SkipClique2 method 5 times
```
   average time: 5.049796891398728e-06
   result set:   {4, 5, 6, 7}
   ```

#### edges from edges3.txt...
#### graph with 2000 nodes

running the BronKerbosch method 5 times
```
   average time: 1.1074151000007988
   result set:   {576, 1954, 1027, 1667, 1396, 6}
   ```
running the Tomita method 5 times
```
   average time: 1.8023619418003363
   result set:   {576, 1954, 1027, 1667, 1396, 6}
   ```
running the Feige method 5 times
```
   average time: 0.017671875000814907
   result set:   {1495, 1174, 1831}
   ```
   
running the SkipClique method 5 times
```
   average time: 0.020467216800898313
   result set:   {576, 1954, 1027, 1667, 1396, 6}
   ```
running the SkipClique2 method 5 times
```
   average time: 0.03755438319931272
   result set:   {576, 1954, 1027, 1667, 1396, 6}
   ```

#### edges from edges4.txt...
#### graph with 4000 nodes

running the BronKerbosch method 5 times
```
   average time: 5.058457575201464
   result set:   {3760, 2, 1042, 793, 1531, 1197}
```
running the Tomita method 5 times
```
   average time: 8.833323083398863
   result set:   {3760, 2, 1042, 793, 1531, 1197}
```
running the Feige method 5 times
```   
   average time: 0.03560558299795957
   result set:   {2946, 1443, 2383, 2582, 2909}
```
running the SkipClique method 5 times
```   
   average time: 0.0633833997999318
   result set:   {3760, 2, 1042, 793, 1531, 1197}
```
running the SkipClique2 method 5 times
```   
   average time: 0.11589485819858965
   result set:   {3760, 2, 1042, 793, 1531, 1197}
```
#### edges from edges5.txt...
#### graph with 10000 nodes

running the BronKerbosch method 5 times
```   
   average time: 38.903657925198786
   result set:   {8960, 1, 1842, 3677, 6045, 6783}
```
running the Tomita method 5 times
```   
   average time: 68.82373612500086
   result set:   {8960, 1, 1842, 3677, 6045, 6783}
```
running the Feige method 5 times
```   
   average time: 0.2249988330004271
   result set:   {459, 1797, 6582, 1019}
```
running the SkipClique method 5 times
   ```
   average time: 0.360057191598753
   result set:   {8960, 1, 1842, 3677, 6045, 6783}
```
running the SkipClique2 method 5 times
```   
   average time: 0.5505748997980845
   result set:   {8960, 1, 1842, 3677, 6045, 6783}
```

# Max-Clique Problem

## Featured Algorithms
### BronKerbosch
### Tomita
### Feige



## References
References 
Feige, U. (2004). Approximating maximum clique by removing subgraphs. SIAM Journal on Discrete Mathematics, 18(2), 219–225. 

Boppana, R.; Halldórsson, M. M. (1992), Approximating maximum independent sets by excluding subgraphs, BIT Numerical Mathematics, 32(2): 180–196. 

A. Jagota, "Approximating maximum clique with a Hopfield network," in IEEE Transactions on Neural Networks, vol. 6, no. 3, pp. 724-735, May 1995 

## Expected Output
Running clique algorithms...

edges from edges1.txt...
graph with 5 nodes
+
running the BronKerbosch method 5 times
+   average time: 1.4829599967924878e-05
+   result set:   {2, 3, 4}
running the Tomita method 5 times
+   average time: 1.1447400174802169e-05
+   result set:   {2, 3, 4}
running the Feige method 5 times
+   average time: 3.809359986917116e-05
+   result set:   {2, 4, 5}

edges from edges2.txt...
graph with 7 nodes
+
running the BronKerbosch method 5 times
+   average time: 2.7436998789198696e-05
+   result set:   {4, 5, 6, 7}
running the Tomita method 5 times
+   average time: 2.3102999693946914e-05
+   result set:   {4, 5, 6, 7}
running the Feige method 5 times
+   average time: 4.914160017506219e-05
+   result set:   {1, 4, 6}

edges from edges3.txt...
graph with 2000 nodes
+
running the BronKerbosch method 5 times
+   average time: 2.1320804190007037
+   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the Tomita method 5 times
+   average time: 3.6336486912005057
+   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the Feige method 5 times
+   average time: 0.15164649580037803
+   result set:   {1831}

edges from edges4.txt...
graph with 4000 nodes
+
running the BronKerbosch method 5 times
+   average time: 9.867383589800738
+   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the Tomita method 5 times
+   average time: 16.924468040799546
+   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the Feige method 5 times
+   average time: 0.8244569213995419
+   result set:   {2383}

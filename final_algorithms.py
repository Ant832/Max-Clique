import math
import time
import random

num_runs = 5

'''
THE WORK OF ANTHONY JANKOVIC, ENOCH GILLMAN, AND KALE GUYMON

---EXPECTED OUTPUT---
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

'''

def parseEdges(filename):
    #returns a structure suitable for the algorithms

    print("importing edges from", filename)
    graph = dict()
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            edge = line.split('|')
            if(len(edge) == 2):
                #for each edge, add endpoints to each-other's set

                a = int(edge[0])
                b = int(edge[1])
                if(not a in graph):
                    graph[a] = set()
                if(not b in graph):
                    graph[b] = set()
                graph[a].add(b)
                graph[b].add(a)

    return graph


def Feige(adj, num_samples=None):
    global num_runs

    print("running the Feige method", num_runs, "times")
    average_time = 0

    for _ in range(num_runs):
        start = time.perf_counter()
        n = len(adj)
        if n == 0:
            return (0.0, 0, set())

        try:
            raw_r = math.floor(math.log(n) / (2 * math.log(math.log(n))))
        except ValueError:
            raw_r = 1
        r = max(1, raw_r)
        r = min(r, n)

        G = {v: set(neigh) for v, neigh in adj.items()}
        for _ in range(r):
            m = len(G)
            if m < 3:
                break
            llm = math.log(math.log(m))
            if llm <= 0:
                break
            thresh = m / llm
            if thresh >= m:
                break
            to_remove = [v for v, neigh in G.items() if len(neigh) < thresh]
            if not to_remove:
                break
            for v in to_remove:
                G.pop(v, None)
                for u in G:
                    G[u].discard(v)

        # 3. clamp r to |G|
        m = len(G)
        if m < r:
            r = max(1, m)

        V = list(G)
        if num_samples is None:
            num_samples = n

        best_clique = set()
        for _ in range(num_samples):
            if len(V) < r:
                break
            S = set(random.sample(V, r))
            C = set(S)
            added = True
            while added:
                added = False
                for v in V:
                    if v not in C and all(v in G[u] for u in C):
                        C.add(v)
                        added = True
            if len(C) > len(best_clique):
                best_clique = C

        average_time += time.perf_counter() - start

        if not best_clique:
            v0 = max(adj, key=lambda x: len(adj[x]))
            best_clique = {v0}

    return (average_time / num_runs, len(best_clique), best_clique)


def Tomita(graph):
    Tomita.graph = graph
    Tomita.clique = set()
    print("running the Tomita method", num_runs, "times")
    def rec_Tomita(R, P, X):
        if len(P) + len(X) == 0 and len(Tomita.clique) < len(R):
            Tomita.clique = R
        else:
            if P or X:
                Pivot_u = max(P.union(X), key=lambda vertex: len(P.intersection(Tomita.graph[vertex])))
                for v in P - Tomita.graph[Pivot_u]:
                    rec_Tomita(
                        R.union({v}),
                        P.intersection(Tomita.graph[v]),
                        X.intersection(Tomita.graph[v])
                    )
                    P.remove(v)
                    X.add(v)
    average_time = 0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        rec_Tomita(set(), set(graph), set())
        average_time += time.perf_counter() - start_time


    return (average_time / num_runs, len(Tomita.clique), Tomita.clique)

def BronKerbosch(graph):
    global num_runs

    BronKerbosch.graph = graph
    BronKerbosch.clique = set()
    print("running the BronKerbosch method", num_runs, "times")
    def rec_BronKerbosch(R, P, X):
        if len(P) + len(X) == 0 and len(BronKerbosch.clique) < len(R):
            BronKerbosch.clique = R
        else:
            for v in list(P):
                rec_BronKerbosch(
                    R.union({v}),
                    P.intersection(BronKerbosch.graph[v]),
                    X.intersection(BronKerbosch.graph[v])
                )
                P.remove(v)
                X.add(v)
    average_time = 0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        rec_BronKerbosch(set(), set(graph), set())
        average_time += time.perf_counter() - start_time


    return (average_time / num_runs, len(BronKerbosch.clique), BronKerbosch.clique)

def main():

    #store algorithms and test graphs in iterable containers
    algorithms = [
        BronKerbosch,
        Tomita,
        Feige
    ]
    graphs = [
        "edges1.txt",
        "edges2.txt",
        "edges3.txt",
        "edges4.txt"
    ]
    for i in range(len(graphs)):
        graphs[i] = (graphs[i], parseEdges(graphs[i]))

    print()
    print("Running clique algorithms...")
    print()

    #run every algorithm on every test graph
    for name, graph in graphs:
        print(f"edges from {name}...\ngraph with {len(graph)} nodes")
        print("+")

        for algorithm in algorithms:
            result = algorithm(graph)
            print("+   average time: " + str(result[0]))
            if(result[1] < 15):
                print("+   result set:   " + str(result[2]))
            else:
                print("+   result len:   " + str(result[1]))
        print()

if __name__ == "__main__":
    main()

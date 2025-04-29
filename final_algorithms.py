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
+   average time: 5.437119980342686e-05
+   result set:   {2, 3, 4}
running the Tomita method 5 times
+   average time: 4.94563952088356e-05
+   result set:   {2, 3, 4}
running the Feige method 5 times
+   average time: 9.60260076681152e-05
+   result set:   {2, 3, 4}
running the SkipClique method 5 times
+   average time: 2.124280435964465e-05
+   result set:   {2, 3, 4}
running the SkipClique2 method 5 times
+   average time: 2.778779889922589e-05
+   result set:   {2, 3, 4}

edges from edges2.txt...
graph with 7 nodes
+
running the BronKerbosch method 5 times
+   average time: 8.88623995706439e-05
+   result set:   {4, 5, 6, 7}
running the Tomita method 5 times
+   average time: 7.667779864277691e-05
+   result set:   {4, 5, 6, 7}
running the Feige method 5 times
+   average time: 0.0002039539976976812
+   result set:   {4, 5}
running the SkipClique method 5 times
+   average time: 3.605099918786436e-05
+   result set:   {4, 5, 6, 7}
running the SkipClique2 method 5 times
+   average time: 5.939459661021829e-05
+   result set:   {4, 5, 6, 7}

edges from edges3.txt...
graph with 2000 nodes
+
running the BronKerbosch method 5 times
+   average time: 6.561483272994519
+   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the Tomita method 5 times
+   average time: 10.045611928400467
+   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the Feige method 5 times
+   average time: 0.44870671498938464
+   result set:   {1495, 1174, 1831}
running the SkipClique method 5 times
+   average time: 0.11966646639921237
+   result set:   {576, 1954, 1027, 1667, 1396, 6}
running the SkipClique2 method 5 times
+   average time: 0.21536145739955828
+   result set:   {576, 1954, 1027, 1667, 1396, 6}

edges from edges4.txt...
graph with 4000 nodes
+
running the BronKerbosch method 5 times
+   average time: 28.49627088320267
+   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the Tomita method 5 times
+   average time: 45.05748925039952
+   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the Feige method 5 times
+   average time: 0.08395806299813557
+   result set:   {2946, 1443, 2383, 2582, 2909}
running the SkipClique method 5 times
+   average time: 0.13447227839787956
+   result set:   {3760, 2, 1042, 793, 1531, 1197}
running the SkipClique2 method 5 times
+   average time: 0.2291649414022686
+   result set:   {3760, 2, 1042, 793, 1531, 1197}


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


def Feige(adj, num_runs=1, num_samples=None):
    print("running the Feige method 5 times")
    n = len(adj)
    if n == 0:
        return (0.0, 0, set())

    if num_samples is None:
        num_samples = n

    try:
        raw_r = math.floor(math.log(n) / (2 * math.log(math.log(n))))
    except ValueError:
        raw_r = 1
    r = max(1, min(raw_r, n))

    total_time = 0.0
    best_overall = set()

    def greedy_fallback(adj):
        v0 = max(adj, key=lambda v: len(adj[v]))
        C = {v0}
        for u in sorted(adj[v0], key=lambda w: len(adj[w]), reverse=True):
            if all(u in adj[w] for w in C):
                C.add(u)
        return C

    start = time.perf_counter()

    G = {v: set(neigh) for v, neigh in adj.items()}
    for _ in range(r):
        m = len(G)
        if m < 3:
            break
        llm = math.log(math.log(m))
        if llm <= 0:
            break
        thresh = math.floor(m / (2 * llm))
        if thresh < 2:
            break

        to_remove = [v for v, neigh in G.items() if len(neigh) < thresh]
        if not to_remove:
            break

        for v in to_remove:
            G.pop(v, None)
        for neighs in G.values():
            for v in to_remove:
                neighs.discard(v)

        m = len(G)
        r_eff = min(r, max(1, m))

        V = list(G)
        best_clique = set()

        for _ in range(num_samples):
            if len(V) < r_eff:
                break
            S = set(random.sample(V, r_eff))
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

        if len(best_clique) <= 1:
            best_clique = greedy_fallback(adj)

        total_time += (time.perf_counter() - start)

        if len(best_clique) > len(best_overall):
            best_overall = best_clique

    avg_time = total_time / num_runs
    return (avg_time, len(best_overall), best_overall)


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

def SkipClique2(graph):
    global num_runs

    SkipClique2.graph = graph
    SkipClique2.clique = set()
    SkipClique2.hop_reset = int(pow(len(graph), 1.5)) + 1
    SkipClique2.hops = SkipClique2.hop_reset
    print("running the SkipClique2 method", num_runs, "times")
    def rec_SkipClique2(R, P, X):
        SkipClique2.hops -= 1
        if len(P) + len(X) == 0 and len(SkipClique2.clique) < len(R):
            SkipClique2.clique = R
            SkipClique2.hops = SkipClique2.hop_reset
        elif(0 < SkipClique2.hops):
            if P or X:
                Pivot_u = max(P.union(X), key=lambda vertex: len(P.intersection(SkipClique2.graph[vertex])))
                for v in P - SkipClique2.graph[Pivot_u]:
                    rec_SkipClique2(
                        R.union({v}),
                        P.intersection(SkipClique2.graph[v]),
                        X.intersection(SkipClique2.graph[v])
                    )
                    P.remove(v)
                    X.add(v)
        else:
                SkipClique2.hops += 1
    average_time = 0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        rec_SkipClique2(set(), set(graph), set())
        average_time += time.perf_counter() - start_time


    return (average_time / num_runs, len(SkipClique2.clique), SkipClique2.clique)



def SkipClique(graph):
    global num_runs

    SkipClique.graph = graph
    SkipClique.clique = set()
    SkipClique.hop_reset = int(pow(len(graph), 1.5)) + 1
    SkipClique.hops = SkipClique.hop_reset
    print("running the SkipClique method", num_runs, "times")
    def rec_SkipClique(R, P, X):
        SkipClique.hops -= 1
        if len(P) + len(X) == 0 and len(SkipClique.clique) < len(R):
            SkipClique.clique = R
            SkipClique.hops = SkipClique.hop_reset
        elif(0 < SkipClique.hops):
            for v in list(P):
                rec_SkipClique(
                    R.union({v}),
                    P.intersection(SkipClique.graph[v]),
                    X.intersection(SkipClique.graph[v])
                )
                P.remove(v)
                X.add(v)
        else:
                SkipClique.hops += 1
    average_time = 0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        rec_SkipClique(set(), set(graph), set())
        average_time += time.perf_counter() - start_time


    return (average_time / num_runs, len(SkipClique.clique), SkipClique.clique)

def main():

    #store algorithms and test graphs in iterable containers
    algorithms = [
        BronKerbosch,
        Tomita,
        Feige,
        SkipClique,
        SkipClique2
    ]
    graphs = [
        "edges1.txt",
        "edges2.txt",
        "edges3.txt",
        "edges4.txt",
        "edges5.txt",
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

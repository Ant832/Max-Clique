import math
import time
from random import random


def parseEdges(filename):
	#returns a structure suitable for the algorithms

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
def feige(adj, num_samples=None):
    print("running the Feige algorithm")
    start = time.time()
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
        if m < 2:
            break
        try:
            thresh = m / math.log(math.log(m))
        except ValueError:
            break
        to_remove = [v for v, neigh in G.items() if len(neigh) < thresh]
        if not to_remove:
            break
        for v in to_remove:
            G.pop(v, None)
            for u in G:
                G[u].discard(v)

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

    elapsed = time.time() - start

    if not best_clique:
        v0 = max(adj, key=lambda x: len(adj[x]))
        best_clique = {v0}

    return (elapsed, len(best_clique), best_clique)

def Tomita(graph):
	Tomita.graph = graph
	Tomita.clique = set()
	print("running the Tomita method")
	def rec_Tomita(R, P, X):
		if len(P) + len(X) == 0 and len(Tomita.clique) < len(R):
			Tomita.clique = R
		else:
			if P or X:
				Pivot_u = max(P.union(X), key=lambda vertex: len(P.intersection(Tomita.graph[vertex])), default=None)
				for v in P - Tomita.graph[Pivot_u]:
					rec_Tomita(
						R.union({v}),
						P.intersection(Tomita.graph[v]),
						X.intersection(Tomita.graph[v])
					)
					P.remove(v)
					X.add(v)
	start_time = time.time()
	rec_Tomita(set(), set(graph), set())
	end_time = time.time()

	return (end_time - start_time, len(Tomita.clique), Tomita.clique)

def BronKerbosch(graph):
	BronKerbosch.graph = graph
	BronKerbosch.clique = set()
	print("running the BronKerbosch method")
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
	start_time = time.time()
	rec_BronKerbosch(set(), set(graph), set())
	end_time = time.time()

	return (end_time - start_time, len(BronKerbosch.clique), BronKerbosch.clique)

def main():
	print("Running clique algorithms...")
	print()

	#store algorithms and test graphs in iterable containers
	algorithms = [
		# BronKerbosch,
		# Tomita,
		feige
	]
	graphs = [
		parseEdges("edges1.txt"),
		parseEdges("edges2.txt"),
		parseEdges("google_graph.txt")
	]

	#run every algorithm on every test graph
	for graph in graphs:
		print(f"graph with {len(graph)} nodes")
		print("+")

		for algorithm in algorithms:
			result = algorithm(graph)
			print("+   secs elapsed: " + str(result[0]))
			if(result[1] < 15):
				print("+   result set:   " + str(result[2]))
			else:
				print("+   result len:   " + str(result[1]))
		print()

if __name__ == "__main__":
	main()

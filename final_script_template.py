import time

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
		BronKerbosch,
		Tomita
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

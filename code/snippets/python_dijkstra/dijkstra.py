def neighbors(graph, vertex):
  '''Returns the neighbors of a given vertex in a given graph list.'''
  ns = set([])
  for v1,v2 in graph:
    if v1 == vertex:
      ns.add(v2)
    elif v2 == vertex:
      ns.add(v1)
    else:
      continue
  return ns

def furthestNode(input):
  '''Finds (in the undirected graph the input list creates) the shortest path 
  to each node and returns the length of the longest.
  Solved using Dijkstra's algorithm as shown and explained here https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode.'''
  vertices = { vertex for edge in input for vertex in edge }

  # Dijkstra BEGIN
  dist = {}
  prev = {}
  Q = set([])
  for v in vertices:
    dist[v] = float('inf')
    prev[v] = 0
    Q.add(v)
  dist[0] = 0
  
  while Q:
    u = min(Q, key=dist.get)
    Q.remove(u)

    for v in [ neighbor for neighbor in neighbors(input, u) if neighbor in Q ]:
      alt = dist[u] + 1
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u
  # Dijkstra END

  reachable = {
      vertex: distance
      for vertex, distance in dist.items() if vertex != 0 and distance != float('inf')
  }

  if reachable:
    return reachable[max(reachable, key=reachable.get)]
  else:
    return 0

assert furthestNode([]) == 0 # check empty list
assert furthestNode([(1,2)]) == 0 # check no node 0
assert furthestNode([(0,1)]) == 1 # check single node
assert furthestNode([(0,2)]) == 1 # check node number makes no difference
assert furthestNode([(1,0)]) == 1 # check order of tuple makes no difference
assert furthestNode([(0,1),(0,2)]) == 1 # check multiple nodes from node 0
assert furthestNode([(0,1),(1,2)]) == 2 # check node chain
assert furthestNode([(0,1),(1,2),(2,0)]) == 1 # check cyclical nodes

assert furthestNode([(0,1),(1,2),(1,3),(2,4),(4,5),(3,4)]) == 4

from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("S", "T", 10),
        ("S", "Y", 5),
        ("T", "X", 1),
        ("Y", "T", 3),
        ("T", "Y", 2),
        ("Y", "Z", 2),
        ("Y", "X", 9),
        ("Z", "S", 7)
    ]

    print "=== Dijkstra ==="
    print dijkstra(edges, "S", "Z")
   



  



G1_NODES = 6
G1_EDGES = [(1, 2), (1, 3), (3, 1), (3, 2), (3, 5), (5, 6), (5,4), (4,6), (4,5), (6,4)] #node1, til-node2

def pagerank(T, edges, q=0.15, max_iter=3):
    # initialization
    L = {}  # holds the number of outgoing edges
    pr = {}  # holds the PageRank score of each node
    for node in range(1, T + 1):
        L[node] = 0
        pr[node] = 1 / T
    for (node1, node2) in edges:
        L[node1] += 1

    for i in range(max_iter):
        # Updating PageRank scores
        new_pr = {}  # holds new PageRank values
        for node in range(1, T + 1):
            new_pr[node] = q / T
            for (node1, node2) in edges:
                if node2 == node:
                    new_pr[node] += (1 - q) * pr[node1] / L[node1]

        # Dealing with "rank sink" nodes
        for node1 in range(1, T + 1):
            if L[node1] == 0:
                # we pretend that it links to all nodes (including itself)
                for node2 in range(1, T + 1):
                    new_pr[node2] += (1 - q) * pr[node1] / T

        # Need to "deep copy" new PageRank values
        pr = dict(new_pr)

        print("Iteration {}:  ".format(i + 1), end="")
        for i in range(T):
            print("{:d}: {:05.3f}   ".format(i + 1, pr[i + 1]), end="")
        print("")  # new line

pagerank(G1_NODES, G1_EDGES, q=0.15)

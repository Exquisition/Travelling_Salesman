'''
Solving the travelling salesman problem via dynamic programming


Written by: Andy Zhou
Dec 31, 2018


psuedocode

Let A = 2-D array, indexed by subsets of {1, 2, ,3, ..., n} that contains 1 and destinations j belongs to {1, 2, 3,...n}
1. Base case:
2.          if S = {0}, then A[S, 1] = 0;
3.          else, A[S, 1] = Infinity.
4.for m = 2, 3, ..., n:   // m = subproblem size
5.    for each subset of {1, 2,...,n} of size m that contains 1:
6.        for each j belongs to S and j != 1:
7.            A[S, j] = the least value of A[S-{j},k]+the distance of k and j for every k belongs to S that doesn't equal to j
8.Return the least value of A[{1,2..n},j]+the distance between j and 1 for every j = 2, 3,...n.


2D dictionary of size number of subsets x number of vertices


'''

import itertools
import numpy as np


# ------------------Initializing adjacency matrix---------------------------------------------

# number of vertices in the graph



def initMatrix(n):
    adjMatrix = np.random.randint(0, 100, size=(n, n), dtype=int)
    np.fill_diagonal(adjMatrix, 0)
    return adjMatrix



def initialize(n):
    '''
    Initializes a dictionary of subsets and pathlength
    :param numVertices:
    :param pathlength:
    :return:
    '''
    setofvertices = [i for i in range(1, n + 1)]

    listSubsets = [[i for i in itertools.combinations(setofvertices, j)] for j in range(0, n)]
    listSubsets = [x for xs in listSubsets for x in xs]

    dict = {k: {i: 'Infinity' for i in range(1, n + 1)} for k in listSubsets}

    return dict


def calculateDistance(pathlist, adjMatrix):
    distance = 0
    for i in range(0, len(pathlist)-1):
        distance += adjMatrix[pathlist[i]-1][pathlist[i+1]-1]
    return distance


def TSP_single_path(vertex, dict, adjMatrix):
    pathlist = []
    pathlist.append(vertex)

    #base case
    firstminvalue = []
    setofvertices = [i for i in range(1, len(adjMatrix) + 1) if i != vertex]
    for v in setofvertices:
        dict[()][v] = adjMatrix[v-1][vertex-1]
        firstminvalue.append((v, dict[()][v]))

    pathlist.append(min(firstminvalue, key=lambda t: t[1])[0])
    #obtain the first vertex to travel to

    for k in range(1, len(adjMatrix)):
        subpaths = []


        # consider sets of k elements
        setofsetsK = [i for i in itertools.combinations(setofvertices, k)]

        for setOfsizeK in setofsetsK:
            #for each subset of size k, fill in the values in dictionary
            for startvertex in setofvertices:

                if startvertex not in setOfsizeK:
                    #for each vertex  g(startvertex, {} size k) =
                         #declare a min
                    '''
                    loop over to get min 
                    '''
                    candidates = []
                    for i in setOfsizeK:


                        setMinus_i = tuple(sorted(set(setOfsizeK).difference(set([i]))))

                        candidates.append(adjMatrix[startvertex-1][i-1] + dict[setMinus_i][i])


                    dict[setOfsizeK][startvertex] = np.min(candidates)


                    #got the minimum at this point

        #for each k, get the minimum vertex



        for set_k in setofsetsK:
            for v2 in setofvertices:
                if vertex not in set_k and v2 not in set_k:
                    subpaths.append((v2, dict[set_k][v2]))

        # finished processing list of tuples of paths

        subpaths.sort(key=lambda x: x[1])

        if subpaths:
            for ele in subpaths:
                if ele[0] in pathlist:
                    continue
                elif ele[0] not in pathlist:
                    pathlist.append(ele[0])






    pathlist.append(vertex)
    pathlist.reverse()


    #finalindex = tuple(sorted(set(setofvertices).difference(set([vertex]))))


    return pathlist


def TSP_solve(adjMatrix):
    paths = []

    for i in range(1, len(adjMatrix) + 1):
        dict = initialize(len(adjMatrix))
        path = TSP_single_path(i, dict, adjMatrix)

        paths.append((path, calculateDistance(path, adjMatrix)))

    min_cost_path = min(paths, key=lambda x: x[1])
    min_cost = min_cost_path[1]

    listOfMinPaths = [path for (path, cost) in paths if cost == min_cost]

    if len(listOfMinPaths) == 1:

        print("The minimum cost tour is: ", min_cost_path[0])
        print("The cost of the tour is: ", min_cost_path[1])

    else:
        print("There is more than one minimum cost tour, they are: ")
        for i, path in enumerate(listOfMinPaths, 1):
            print("Tour {}: {}".format(i, path))
        print("The cost of the tours are all: ", min_cost_path[1])


    return min_cost_path



if __name__ == '__main__':

    matrix = np.array([[0,2,9,10], [1,0,6,4], [15, 7, 0, 8], [6,3,12,0]])
    TSP_solve(matrix)

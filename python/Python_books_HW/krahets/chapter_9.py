''' Графы '''
class GraphAdjMat:
    def __init__(self, vertices: list[int], edges: list[list[int]]):
        self.vertices: list[int] = vertices
        self.adj_mat: list[list[int]] = []
        for val in vertices: self.add_vertex(val)
        for e in edges: self.add_edge(e[0], e[1])

    def size(self) -> int: return len(self.vertices)

    def add_vertex(self, val: int):
        n = self.size()
        self.vertices.append(val)
        new_row = [0] * n
        self.adj_mat.append(new_row)
        for row in self.adj_mat: row.append(0)

    def remove_vertex(self, index: int):
        if index >= self.size(): raise IndexError()
        self.vertices.pop(index)
        self.adj_mat.pop(index)
        for row in self.adj_mat: row.pop(index)

    def add_edge(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j: raise IndexError()
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j: raise IndexError()

    def print(self):
        print('Список вершин =', self.vertices)
        print('Матрица смежности = ')
        print(self.adj_mat)

class Vertex:
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.val == other.val
        return False

    def __repr__(self):
        return f"Vertex({self.val})"
    
class GraphAdjList:
    def __init__(self, edges: list[list[Vertex]]):
        self.adj_list = dict[Vertex, list[Vertex]]()
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def size(self) -> int: return len(self.adj_list)

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2: raise ValueError()
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2: raise ValueError()
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)

    def add_vertex(self, vet: Vertex):
        if vet in self.adj_list:
            return
        self.adj_list[vet] = []
    
    def remove_vertex(self, vet: Vertex):
        if vet not in self.adj_list: return ValueError()
        self.adj_list.pop(vet)
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)

    def print(self): 
        print('Список смежности: ')
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f'{vertex.val}: {tmp}, ')

''' BFS - broad first search - поиск в ширину'''
from collections import deque
def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    res = []
    visited = set[Vertex]([start_vet])
    que = deque[Vertex]([start_vet])
    while len(que) > 0:
        vet = que.popleft()
        res.append(vet)
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited: continue
            que.append(adj_vet)
            visited.add(adj_vet)
    return res

''' DFS - depth first search - поиск в глубину '''
def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    res.append(vet)
    visited.add(vet)
    for adj_vet in graph.adj_list[vet]:
        if adj_vet in visited: continue
        dfs(graph, visited, res, adj_vet)

def graph_dfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    res = []
    visited = set[Vertex]()
    dfs(graph, visited, res, start_vet)
    return res
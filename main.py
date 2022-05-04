from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def weight_helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            distance, node, counter = heappop(frontier)
            if node in visited:
                return weight_helper(visited, frontier)
            else:
                visited[node] = (distance, counter)
                counter += 1
                for neighbor, weight in graph[node]:
                    heappush(frontier, (distance + weight, neighbor, counter))                
                return weight_helper(visited, frontier)
    
        
    frontier = []
    heappush(frontier, (0, source, 0))
    visited = dict() 
    return weight_helper(visited, frontier)
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    def bfs_serial_helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            node = frontier.popleft()
            visited.add(node)
            frontier.extend(filter(lambda n: n not in visited, graph[node]))
            return bfs_serial_helper(visited, frontier)

    frontier = deque()
    frontier.append(source)
    visited = set()
    return bfs_serial_helper(visited, frontier)

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    pass

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'

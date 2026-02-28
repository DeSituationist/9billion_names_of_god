def find_adjacent_nodes(adj_matrix: list[list[int]], start_node: int) -> list[int]:
    '''Function that finds adjacent nodes in graphs to given node'''
    all_columns = [[adj_matrix[j][i] for j in range(len(adj_matrix[0]))] for i in range(len(adj_matrix[0]))]
    return [i for i in range(len(all_columns[start_node])) if all_columns[start_node][i] == 1]
print(find_adjacent_nodes([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 0))
print(find_adjacent_nodes([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 1))
print(find_adjacent_nodes([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]], 1))
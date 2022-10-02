'''
detect a cycle if exist in given graph using dfs

idea is to carry a prev node value to compare while checking visited array

'''



from lib2to3.pytree import Node
from operator import truediv
from typing import Dict, List


def detect_cycle(adj_list: Dict[int, List[int]], num_of_nodes: int) -> bool:
    visited_arr = [0] * num_of_nodes
    

    def dfs_cycle_check(node,adj_list, visited_arr: List[int], prev_node: int) -> bool:

        visited_arr[node] = 1
        adj_nodes = adj_list.get(node)

        for n in adj_nodes:
            
            if not visited_arr[n]:
               
                if dfs_cycle_check(n, adj_list, visited_arr, node):
                    return True

            elif n != prev_node:
                return True 

        return False        
       
        



    for key in adj_list:
        # prev_node = -1
        if not visited_arr[key]:

            if dfs_cycle_check(key,adj_list, visited_arr, -1):
                return True

    return False            


adj_list = {
    0 : [1],
    1 : [0,2,4],
    2 : [1,3],
    3 : [4,2],
    4 : [1,3]
}

adj_list ={
    0 : [],
    1 : [2],
    2 : [1,3],
    3 : [2]
}
no_of_nodes = 5

ans = detect_cycle(adj_list, no_of_nodes)
print(f'cycle detected for given undirected graph is : {ans}')

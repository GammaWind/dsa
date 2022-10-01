''''
dfs traversal of below given graph
0
|
1 --- 2----5   6---7
|              |
|              |
4-----3        8
Tc O(N + E (for edges))
spc comp: O(N) for queue that we are using + O(N) for the set aswell

'''

from typing import Dict, List, Set


def dfs_traversal(adj_list: Dict[int, List[int]]):
    vistied_set = set()
    ans = []

    def dfs(node, adj_list: Dict[int, List[int]], ans: List[int], vistied_set: Set[int]):
        
        ans.append(node)
        

        adj_nodes = adj_list.get(node)
        for n in adj_nodes:
            if n not in vistied_set:
                vistied_set.add(n)
                dfs(n, adj_list, ans, vistied_set)
    for key in adj_list:
        print(f'key {key}')
        if key not in vistied_set:
            vistied_set.add(key)
            dfs(key, adj_list, ans, vistied_set)

    return ans 


#setup to convert graph to ad matrix
graph = {
  5 : [3,7],
  3 : [2,4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}


ans = dfs_traversal(graph)
print(ans)

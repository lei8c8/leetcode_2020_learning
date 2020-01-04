class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        cloned_node = Node(node.val, [])
        self.visited[node] = cloned_node
        if node.neighbors:
            cloned_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return cloned_node

        
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        seen = set(['0000'])
        queue = deque([('0000', 0)])
        while queue:
            node, level = queue.popleft()
            if node == target:
                return level 
            if node in dead:
                continue
            for n in self.generate_nei(node):
                if n not in seen:
                    seen.add(n)
                    queue.append((n, (level + 1)))
        return -1

    def generate_nei(self, node):
        for i in range(4):
            val = int(node[i])
            for x in (-1, 1):
                y = (val + x) % 10
                yield node[:i] + str(y) + node[i+1:]
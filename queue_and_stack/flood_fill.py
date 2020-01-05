from collections import deque 

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        org_color = image[sr][sc]
        if org_color == newColor:
            return image
        self.bfs_fill(image, sr, sc, newColor, org_color)
        return image
        
    def bfs_fill(self, image, i, j, newColor, orgColor):
        queue = deque([(i, j)])
        while queue:
            d1, d2 = queue.popleft()
            if 0 <= d1 < len(image) and 0 <= d2 < len(image[0]) and image[d1][d2] == orgColor:
                image[d1][d2] = newColor
                dirs = [(d1,d2+1),(d1,d2-1),(d1-1,d2),(d1+1,d2)]
                for x1, y1 in dirs:
                    queue.append((x1,y1))
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        original_color = image[sr][sc]


        def dfs(x, y):
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == original_color:
                image[x][y] = color
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
        
        dfs(sr, sc)
        return image

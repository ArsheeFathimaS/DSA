class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update each element with its value + min of two adjacent elements below
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
        
        return triangle[0][0]

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for row in grid:
            for num in row:
                if num < 0:
                    count += 1
        return count


if __name__ == "__main__":
    grid = [
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, -1, -2, -3],
        [-1, -2, -3, -4],
    ]
    print(Solution().countNegatives(grid))

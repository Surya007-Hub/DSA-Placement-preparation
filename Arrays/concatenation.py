class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans


if __name__ == "__main__":
    # simple test/example
    nums = [1, 2, 3]
    print(Solution().getConcatenation(nums))
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        result = []
        for num in nums:
            total += num
            result.append(total)
        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().runningSum(nums))
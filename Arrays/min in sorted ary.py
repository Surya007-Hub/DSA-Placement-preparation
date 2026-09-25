class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            return -1

        smallest = nums[0]
        for num in nums[1:]:
            if num < smallest:
                smallest = num
        return smallest


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(Solution().findMin(nums))

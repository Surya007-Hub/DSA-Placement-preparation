from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None

        for num in nums:
            if num in (first, second, third):
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num

        if third is None:
            return first
        return third


if __name__ == "__main__":
    print(Solution().thirdMax([3, 2, 1]))
    print(Solution().thirdMax([1, 2]))
    print(Solution().thirdMax([2, 2, 3, 1]))

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = 0
        count2 = 0

        set_nums2 = set(nums2)
        set_nums1 = set(nums1)

        for num in nums1:
            if num in set_nums2:
                count1 += 1

        for num in nums2:
            if num in set_nums1:
                count2 += 1

        return [count1, count2]


if __name__ == "__main__":
    nums1 = [3, 1, 2, 3]
    nums2 = [1, 2, 4]
    result = Solution().findIntersectionValues(nums1, nums2)
    print(f"Intersection values: {result}")

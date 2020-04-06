from typing import List

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Source: https://leetcode.com/problems/median-of-two-sorted-arrays/
Tutorial: https://www.youtube.com/watch?v=9yrUs-61ofc
"""


# The space complexity of this solution can be optimized by using indexes.
class Solution:

    @staticmethod
    def find_median_of_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)

        if total_length % 2 == 0:
            return (Solution.find_kth_element(total_length // 2, nums1, nums2) + Solution.find_kth_element(
                total_length // 2 - 1, nums1, nums2)) / 2
        else:
            return Solution.find_kth_element(total_length // 2, nums1, nums2)

    # If a = [1, 2, 3] and k = 1, the k-th element is a[k] = 2
    @staticmethod
    def find_kth_element(k: int, nums1: List[int], nums2: List[int]) -> int:

        if len(nums1) == 0:
            return nums2[k]

        if len(nums2) == 0:
            return nums1[k]

        mid1 = len(nums1) // 2
        mid2 = len(nums2) // 2

        if mid1 + mid2 < k:  # right half
            if nums1[mid1] > nums2[mid2]:
                return Solution.find_kth_element(k - mid2 - 1, nums1, nums2[mid2 + 1:])
            else:
                return Solution.find_kth_element(k - mid1 - 1, nums1[mid1 + 1:], nums2)
        else:  # left half
            if nums1[mid1] > nums2[mid2]:
                return Solution.find_kth_element(k, nums1[:mid1], nums2)
            else:
                return Solution.find_kth_element(k, nums1, nums2[:mid2])

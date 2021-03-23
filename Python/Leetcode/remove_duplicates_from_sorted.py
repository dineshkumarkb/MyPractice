"""
Given a sorted array nums,
remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
"""
from collections import Counter

class Solution:

    def remove_duplicates(self, nums):

        count = 0
        for i in range(len(nums)-1):
            if nums[count] == nums[count+1]:
                nums.remove(nums[count])
            else:
                count += 1

        print(len(nums))



if __name__ == "__main__":
    s = Solution()
    s.remove_duplicates([0,0,1,1,1,2,2,3,3,4])
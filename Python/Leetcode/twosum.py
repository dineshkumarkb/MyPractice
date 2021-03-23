"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

class TwoSum(object):
    
    def __init__(self, nums: list, target: int):
        self.nums = nums
        self.target = target
        self.get_indices()

    def get_indices(self):

        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    print(i, j)


if __name__ == '__main__':
    t = TwoSum(nums=[2,7,11,15], target=9)
    t = TwoSum(nums=[3, 2, 4], target=6)
    t = TwoSum(nums=[3,3], target=6)
    t = TwoSum(nums=[3,2,3], target=6)

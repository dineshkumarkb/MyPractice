"""

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""

def jump_prob(nums):

    n = len(nums)

    if n <= 1:
        return 0

    # Initialize max reach value
    max_reach = step = nums[0]

    jump = 1

    for i in range(1, n):

        if i == n-1:
            return jump

        max_reach = max(max_reach, i + nums[i])

        print(f" Iteration : {i}, element: {nums[i]} ")
        print(f" max reach: {max_reach} ")

        step -= 1
        print(f" Step decremented : {step}")

        if step == 0:
            jump += 1
            print(f" Jump value: {jump}")

            if i >= max_reach:
                print(f"{i} >= {max_reach}")
                return -1

            step = max_reach - i
            print(f" step:{step}")

    return -1


print(jump_prob([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(jump_prob([2,3,1,1,4]))
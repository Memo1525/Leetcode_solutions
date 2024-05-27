"""
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
"""
# first approach using example 3
is_greater_or_equal = 0
nums = [0,4,3,0,4]
for i in range(len(nums)+1):
    is_greater_or_equal = 0
    for j in range(len(nums)):
        if i <= nums[j]:
            is_greater_or_equal +=1
    if is_greater_or_equal == i:
        print(i)
        break
print(-1)

#this works but a think is not fast enough too bee optimal 

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        is_greater_or_equal = 0
        nums = [0,4,3,0,4]
        for i in range(len(nums)+1):
            is_greater_or_equal = 0
            for j in range(len(nums)):
                if i <= nums[j]:
                    is_greater_or_equal +=1
            if is_greater_or_equal == i:
                return i

        return -1

implementation = Solution()

print(implementation.specialArray(nums))

    
    

"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Solution: https://www.youtube.com/watch?v=re7fhVyKWZI&t=11s
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []

        for i in nums:
            pos = abs(i) - 1
            if nums[pos] > 0:
                nums[pos] *= -1
                    
        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i + 1)
        
        return missing
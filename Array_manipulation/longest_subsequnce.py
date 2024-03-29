Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        s1=0
        for i in nums:
            
            s=1
            while (i+s in nums) and i-1 not in nums:
               s+=1
               
            s1=max(s,s1)
        return s1
# beats 70%
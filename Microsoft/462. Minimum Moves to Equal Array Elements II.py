class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        n=len(nums)
        target=nums[n//2]

        return sum(abs(target-n)for n in nums)

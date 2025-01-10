class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            arr = nums.copy()
            for j in range(len(nums) - i):
                arr.pop(i)
                if arr == sorted(set(arr)):
                    res += 1
        
        return res

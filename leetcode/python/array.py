# https://leetcode.com/problems/move-zeroes/
class MoveZeros:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nzi = 0
        for i, v in enumerate(nums):
            if v != 0:
                if nzi != i:
                    nums[nzi] = v
                nzi += 1

        for i in range(nzi, len(nums)):
            nums[i] = 0

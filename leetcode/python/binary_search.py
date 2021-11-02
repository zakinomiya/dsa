


# https://leetcode.com/problems/search-insert-position/
class SearchInsert:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) -1 
        while l <= r:
            med = (l+r) // 2
            if nums[med] == target:
                return med
            elif nums[med] > target:
                r -= 1
            else:
                l += 1

        return r if r > l else l

        

class MaxSubArray:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0] if nums[0] > 0 else 0

        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + nums[i] if nums[i] > 0 else dp[i-1]

        return max(dp)

if __name__ == "__main__":
    m = MaxSubArray()
    r = m.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])
    print(r)
    assert(r == 6)


class SubarraySum:
    def subarraySum(self, nums: list[int], k: int) -> int:
        p_sum = {0:1}

        s = 0
        cnt = 0
        for n in nums:
            s += n

            if s-k in p_sum:
                cnt += p_sum[s-k]

            if s in p_sum:
                p_sum[s] += 1
            else:
                p_sum[s] = 1

        return cnt


if __name__ == "__main__":
    s = SubarraySum()
    print(s.subarraySum([1, 1, 1], 2))
    print(s.subarraySum([1, 2, 3], 3))
    print(s.subarraySum([1], 0))
    print(s.subarraySum([-1, -1, 1], 0))
    print(s.subarraySum([1, -1, 0], 0))

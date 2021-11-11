# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from heapq import heappop, heappush


class KSmallest:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if len(nums1) * len(nums2) <= k:
            return [[n1, n2] for n1 in nums1 for n2 in nums2]

        ans = []
        min_heap = []
        # beacause nums1[0] + nums2[0] is always the smallest sum
        heappush(min_heap, [nums1[0] + nums2[0], 0, 0])
        visited = []
        while len(ans) < k:
            _, i, j = heappop(min_heap)
            if (i, j) in visited:
                continue
            ans.append([nums1[i], nums2[j]])
            visited.append((i,j))
            if len(nums1) > i + 1 and len(nums2) > j:
                heappush(min_heap, [nums1[i+1]+nums2[j], i+1, j])
            if len(nums1) > i and len(nums2) > j + 1:
                heappush(min_heap, [nums1[i]+nums2[j+1], i, j+1])

        return ans


if __name__ == "__main__":
    s = KSmallest()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
    print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
    print(s.kSmallestPairs([1, 2], [3], 3))
    print(s.kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 3))
    print(s.kSmallestPairs([-10, -4, 0, 0, 6], [3, 5, 6, 7, 8, 100],  10))

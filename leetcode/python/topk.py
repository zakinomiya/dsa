from collections import Counter
import heapq

# https://leetcode.com/problems/top-k-frequent-elements/
class TopK:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = {}

        for n in nums:
            if n not in h:
                h[n] = {
                    "val": n,
                    "cnt": 1,
                }
            else:
                h[n]["cnt"] += 1

        return [ n["val"] for n in sorted(h.values(), key=lambda x:x["cnt"], reverse=True)][:k]

    def topKFrequent2(self, nums: list[int], k: int) -> list[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(n=k, iterable=count.keys(), key=count.get) 

if __name__ == "__main__":
    t = TopK()
    print(t.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(t.topKFrequent2([1, 1, 1, 2, 2, 3], 2))

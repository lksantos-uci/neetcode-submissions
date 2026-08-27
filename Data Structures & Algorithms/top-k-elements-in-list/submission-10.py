class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        bucket = [[] for i in range(len(nums) + 1)]
        for n, f in freq.items():
            bucket[f].append(n)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                if len(res) == k:
                    break
                res.append(n)
        return res
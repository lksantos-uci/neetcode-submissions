class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        bucket = [[] for i in range(len(nums) + 1)]
        for num, frequency in freq.items():
            bucket[frequency].append(num)
        output = []
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                if len(output) == k:
                    break
                output.append(n)
        return output

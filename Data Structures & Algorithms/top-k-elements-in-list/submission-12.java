class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Hashmap to map # to freq
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        // Bucket sort each number by freq
        List<Integer>[] bucket = new List[nums.length + 1];
        freq.forEach((key, value) -> {
            if (bucket[value] == null) {
                bucket[value] = new ArrayList<>();
            }
            bucket[value].add(key);
        });
        int[] res = new int[k];
        int count = 0;
        // Starting from most freq bucket, return the output
        for (int index = bucket.length - 1; index != -1; index--) {
            if (bucket[index] == null) continue;
            for (int num : bucket[index]) {
                res[count++] = num;
                if (count == k) {
                    return res;
                }
            }
        }
        return res;
    }
}

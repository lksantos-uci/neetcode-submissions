class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        for (int index = 0; index < nums.length; index++) {
            int num = nums[index];
            if (hashmap.containsKey(target - num)) {
                return new int[] { hashmap.get(target-num), index };
            }
            hashmap.put(num, index);
        }
        return new int[0];
    }
}
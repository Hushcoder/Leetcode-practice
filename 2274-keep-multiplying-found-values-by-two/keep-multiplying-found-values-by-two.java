class Solution {
    public int findFinalValue(int[] nums, int original) {
        int n = nums.length;
        
        HashSet<Integer> map = new HashSet<>();

        for(int it : nums){
            map.add(it);
        }

        while (map.contains(original)) {
            original *= 2;
        }
        return original;
    }
}
class Solution {
    public int findFinalValue(int[] nums, int original) {
        int n = nums.length;
        // int val = original;
        HashMap<Integer , Integer> map = new HashMap<>();
        for(int it : nums){
            map.put(it , 1);
        }

        for(int i =0; i<n; i++){
            if(map.containsKey(original)){
                original = original*2;
            }
        }
        return original;
    }
}
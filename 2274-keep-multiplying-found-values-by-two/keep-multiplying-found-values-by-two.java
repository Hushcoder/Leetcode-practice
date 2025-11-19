class Solution {
    public int findFinalValue(int[] nums, int original) {
        int n = nums.length;
        int val = original;

        for(int i=0; i<n; i++){
            for(int j = 0; j<n; j++){
                if(nums[j] == val){
                val = 2*val;
                }
            }
        }
        return val;
    }
}
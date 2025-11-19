class Solution {
    public int findFinalValue(int[] nums, int original) {
        int n = nums.length;
        int val = original;

        // for(int i=0; i<n; i++){
        //     for(int j = 0; j<n; j++){
        //         if(nums[j] == val){
        //         val = 2*val;
        //         }
        //     }
        // }
        // return val;
        HashMap<Integer , Integer> map = new HashMap<>();
        for(int it : nums){
            map.put(it , 1);
        }

        for(int i =0; i<n; i++){
            if(map.containsKey(val)){
                val = val*2;
            }
        }
        return val;
    }
}
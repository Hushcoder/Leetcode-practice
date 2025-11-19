class Solution {
    public int findFinalValue(int[] nums, int original) {
        int n = nums.length;
        
        HashSet<Integer> map = new HashSet<>();

        for(int it : nums){
            map.add(it);
        }

        for(int i =0; i<n; i++){
            if(map.contains(original)){
                original = original*2;
            }
        }
        return original;
    }
}
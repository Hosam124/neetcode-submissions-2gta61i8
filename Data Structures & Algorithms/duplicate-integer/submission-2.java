class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer>mp = new HashMap<>();

        for(int i : nums){
            if(mp.containsKey(i)){
                return true;
            }
            mp.put(i,mp.getOrDefault(i,0)+1);
        }
        return false;

    }
}
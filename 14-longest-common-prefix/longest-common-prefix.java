class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        Arrays.sort(strs);

        String first = strs[0];
        String last = strs[strs.length-1];

        int min = first.length() < last.length() ? first.length() : last.length();
        int j = 0;
        for(int i=0; i< min ;i++)
        {
            if(first.charAt(i) != last.charAt(i))
            break;
            j++;
        }

        return strs[0].substring(0,j);
    }
}
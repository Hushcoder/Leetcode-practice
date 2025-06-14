class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String prefix = "";
        // Loop through characters of the first string
        for (int i = 0; i < strs[0].length(); i++) {
            char currentChar = strs[0].charAt(i);
            
            // Loop through the rest of the strings
            for (int j = 1; j < strs.length; j++) {
                // Check if index exceeds length or character mismatches
                if (i >= strs[j].length() || strs[j].charAt(i) != currentChar) {
                    return prefix;  // Return prefix found so far
                }
            }
            prefix += currentChar; // Add matching character
        }
        return prefix;

    }
}
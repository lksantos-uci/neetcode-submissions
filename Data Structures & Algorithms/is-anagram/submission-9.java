class Solution {
    public boolean isAnagram(String s, String t) {
        // Check if they are of the same length
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (sMap.containsKey(s.charAt(i)))
                sMap.put(s.charAt(i), sMap.get(s.charAt(i)) + 1);
            else
                sMap.put(s.charAt(i), 0);
            if (tMap.containsKey(t.charAt(i)))
                tMap.put(t.charAt(i), tMap.get(t.charAt(i)) + 1);
            else
                tMap.put(t.charAt(i), 0);
        }
        return sMap.equals(tMap);
    }
}

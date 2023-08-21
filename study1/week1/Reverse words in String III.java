class Reverse words in String III {

    public String reverseWords(String s) {
        String res = "";                                // space complexity O(1)

        for(String a : s.split(" ")){                   // linear time complexity O(n), n is the length of the input String  
            StringBuffer sb = new StringBuffer(a);      // space complexity O(m), m is the length of a particular word
            String reverse = sb.reverse().toString();   // linear time complexity O(m)  
            res += reverse + " ";                       // constant time complexity O(1)
        }
        res = res.stripTrailing();                      // constant time complexity O(1)  
        return res;                                     // space complexity O(n)
    }
// Time Complexity = O(n*m)
// Space Complexity = O(n+m) = O(n)
}

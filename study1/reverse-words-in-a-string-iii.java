class Solution {
    public String reverseWords(String s) {
        //check if length of s is 1 or s is null
        //s.length() is an operation that returns the length of the string s,
        //so it takes O(1) time to check the length
        if (s.length() <= 1 || s == null) {
            return s;
        }
        //split() -> performed proportionally to the length of the string
        //if the length of String is n, so it takes O(n) time to split the String
        //size of this splited array is proportional to the number of words in input String
        //so the size of the splited array is O(n).
        String[] splitedArr = s.split(" ");
        //create new reversed Array of input String
        //size of this array is proportional to the number of words in splited string array
        //so the size of the reversed array is O(n).
        String[] reversedArr = new String[splitedArr.length];

        for (int i = 0; i < splitedArr.length; i++) {
            //create a Stringbuffer to use the reverse function
            //size of this sb is proportional to the length of each word 
            //and it depends on the maximum word length
            //if length of maximum word is m -> size of sb is O(m)
            StringBuffer sb = new StringBuffer(splitedArr[i]);
            //add the inverted String to the new String Array
            //reversing each word takes time proportional to the length of the word
            //if there is n words in the Strings -> it takes O(n) time to reverse the word
            reversedArr[i] = sb.reverse().toString();
        }
        //combine String Arrays into Strings using the join function
        //if there is n word in reversedArr -> it takes also O(n) time to join the word
        return String.join(" ", reversedArr);

        //So the total time complexity is O(n)
        //And the space complexity is also O(n), because of always m<=n?..
    }
}

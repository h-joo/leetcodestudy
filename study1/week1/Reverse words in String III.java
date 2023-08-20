class Reverse words in String III {
    public String reverseWords(String s) {
        String res = "";
       
        for(String a : s.split(" ")){
            StringBuffer sb = new StringBuffer(a);
            String reverse = sb.reverse().toString();
            res += reverse + " ";
        }
        res = res.stripTrailing();
        return res;
    }
}

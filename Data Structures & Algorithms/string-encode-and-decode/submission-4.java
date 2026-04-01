class Solution {

    public String encode(List<String> strs) {

        StringBuilder encode = new StringBuilder();

        for(String s : strs){
            encode.append(s.length()).append("#").append(s);
        }
        return encode.toString();
    }

    public List<String> decode(String str) {
        List<String> decode = new ArrayList<>();
        int idx = 0;
        while(idx < str.length()){
            StringBuilder len = new StringBuilder();
            while (str.charAt(idx)>= '0' && str.charAt(idx)<= '9' && str.charAt(idx)!= '#'){
                len.append(str.charAt(idx));
                idx++;
            }
            int strLen = Integer.parseInt(len.toString()) ;
            String newStr = new String();
            newStr = str.substring(idx+1,idx+strLen+1);
            decode.add(newStr);
            idx+=strLen+1;
        }
        return decode;

    }
}

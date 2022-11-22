import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";
        String uppercase = "";

        char[] charArr = s.toCharArray();
        Arrays.sort(charArr);

        for(int i=0; i< charArr.length; i++){
            if(charArr[charArr.length-i-1] <= 90 ){
                uppercase += charArr[charArr.length-i-1];
            } else {
                answer += charArr[charArr.length-i-1];
            }
        }
        return answer + uppercase;
    }
}
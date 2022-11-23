class Solution {
    public String solution(String s, int n) {
        String answer = "";

        char[] charArr = s.toCharArray();
        for(int i=0; i<charArr.length; i++){
            if(charArr[i] == 32){
                answer += " ";
                continue;
            }
            int num = 0;
            if(charArr[i] >= 97 ){
                num = charArr[i] + n;
                if(num > 122){
                    num = 97 + ((num-97) % 26);
                }
            } else {
                num = charArr[i] + n;
                if(num > 90){
                    num = 65 + ((num-65) % 26);
                }
            }
            char charChange = (char) num;
            answer += charChange;
        }

        return answer;
    }
}
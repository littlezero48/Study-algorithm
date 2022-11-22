class Solution {
    public int solution(String input) {
        int answer = 0;
        String answer1 = "";

        String numStr = "";
        String numName_get = "";
        char[] charArr = input.toCharArray();

        for(int i=0; i<charArr.length+1; i++){
            if (i == charArr.length) {
                answer1 += nameGet(numName_get, "");
            } else if(!Character.isDigit(charArr[i])){
                numName_get += charArr[i];
            } else if (Character.isDigit(charArr[i]) && numName_get== ""){
                answer1 += Character.toString(charArr[i]);
            } else {
                answer1 += nameGet(numName_get, "") + Character.toString(charArr[i]);
                numName_get="";
            }
        }

        answer = Integer.parseInt(answer1);

        return answer;
    }

    public static String nameGet(String s, String answer){
        String[] numName = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        for(int i=0; i<numName.length; i++){

            int numNameLen = numName[i].length();

            if(s.length() >= numName[i].length()){
                if(numName[i].equals(s.substring(0,numNameLen))){
                    answer += Integer.toString(i);
                    s = s.substring(numNameLen);
                    break;
                }
            } else {
                continue;
            }
        }

        if(s.equals("")){
            return answer;
        }

        return nameGet(s,answer);
    }
}
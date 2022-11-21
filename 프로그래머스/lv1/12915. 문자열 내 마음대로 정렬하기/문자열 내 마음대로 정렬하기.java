import java.util.Arrays;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];

        for(int i=0; i<strings.length; i++){
            if(n == 0) {
                answer[i] = strings[i] + i;
            } else if (n == strings[i].length()){
                answer[i] = strings[i].substring(n,n+1) + strings[i].substring(0,n) + i;
            } else {
                answer[i] = strings[i].substring(n,n+1) + strings[i].substring(0,n) + strings[i].substring(n+1)  + i;
            }
        }
        Arrays.sort(answer);

        for(int j=0; j<answer.length; j++){

            int answerLen = answer[j].length();
            int index = Integer.parseInt(answer[j].substring(answerLen-1));
            answer[j] = strings[index];
        }

        return answer;
    }
}
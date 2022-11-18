public class Solution {
    public int solution(int n) {
        int answer = 0;

        String a = Integer.toString(n);
        String[] s_arr = a.split("");

        for(int i=0; i<s_arr.length; i++){
            answer += Integer.parseInt(s_arr[i]);
        }

        return answer;
    }
}
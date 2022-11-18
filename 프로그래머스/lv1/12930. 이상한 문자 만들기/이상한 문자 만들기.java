class Solution {
    public String solution(String s) {
        String answer = "";
        int cnt = 0;
        String[] s_arr = s.split("");

        for (int i=0; i<s_arr.length; i++){
            if(s_arr[i].equals(" ")){
                cnt = 0;
                answer += " ";
            } else {
                answer += (cnt%2==0) ? s_arr[i].toUpperCase() : s_arr[i].toLowerCase();
                cnt++;
            }
        }
        return answer;
    }
}
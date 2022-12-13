class Solution {
    public int solution(int n) {
        int sum = 0;
        String[] s_list = String.valueOf(n).split("");
        for(int i=0; i<s_list.length; i++){
            sum += Integer.parseInt(s_list[i]);
        }
        return sum;
    }
}
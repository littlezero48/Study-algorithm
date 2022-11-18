class Solution {
    public int[] solution(long n) {
        
        String numString = Long.toString(n);
        int numLen = numString.split("").length;
        int[] answer = new int[numLen];
        for(int i=0; i<numLen; i++){
            answer[i] = (int) (n % 10);
            n /= 10;
        }
        return answer;
    }
}
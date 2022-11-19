class Solution {
    public long solution(long n) {
        long answer = 0;
        double root = Math.sqrt((double)n);
        if((root - (int)root) == 0){
            answer = Double.valueOf(Math.pow(root+1,2)).longValue();
        } else {
            answer = -1;
        }
        return answer;
    }
}
class Solution {
    public int solution(int n) {
        int answer = 0;
        int num = 0;
        String numString = "";
        while(n > 0){
            num = n % 3;
            n /= 3;
            numString += String.valueOf(num);
        }

        String numOne = "";
        int numStringLen = numString.length();
        for(int i=0; i<numStringLen; i++){
            numOne = numString.substring(numStringLen-1-i, numStringLen-i);
            int squareNum = (int) Math.pow(3, i);
            int multiply = Integer.parseInt(numOne);
            answer += squareNum * multiply;
        }

        return answer;
    }
}
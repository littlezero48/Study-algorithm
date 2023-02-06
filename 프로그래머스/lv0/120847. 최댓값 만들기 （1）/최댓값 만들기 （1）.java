class Solution {
    public int solution(int[] numbers) {
        int max1 = 0;
        int max2 = 0;
        for(int i : numbers){
            if(i > max1){
                if (i > max2){
                    max1 = max2;
                    max2 = i;
                } else {
                    max1 = i;
                }
            }
        }
        return max1*max2;
    }
}
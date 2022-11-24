class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        int MaxNum = 0;
        int MaxIdx = 0;
        
        for(int i=0; i<array.length; i++){
            if(i==0){
                MaxNum = array[i];
            } 
            if(MaxNum < array[i]){
                MaxNum = array[i];
                MaxIdx = i;
            }
        }
        
        answer[0] = MaxNum;
        answer[1] = MaxIdx;
        
        return answer;
    }
}
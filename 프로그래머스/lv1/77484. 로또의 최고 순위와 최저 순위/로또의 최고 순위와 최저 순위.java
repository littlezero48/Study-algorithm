class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int zeroCnt = 0;
        int winNumCnt = 0;
        for(int i=0; i<lottos.length; i++){
            for(int j=0; j<win_nums.length; j++){
                if(lottos[i] == 0){
                    zeroCnt++;
                    break;
                }
                if(lottos[i] == win_nums[j]){
                    winNumCnt++;
                }
            }
        }
        
        answer[0] = winNumCnt + zeroCnt;
        answer[1] = winNumCnt + 0;

        for(int k=0; k<2; k++){
            switch (answer[k]) {
                case 6 :
                    answer[k] = 1;
                    break;
                case 5:
                    answer[k] = 2;
                    break;
                case 4:
                    answer[k] = 3;
                    break;
                case 3:
                    answer[k] = 4;
                    break;
                case 2:
                    answer[k] = 5;
                    break;
                case 1:
                case 0:
                    answer[k] = 6;
            }
        }

        return answer;
    }
}
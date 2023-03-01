import java.util.ArrayList;
class Solution {
   public int[] solution(int[] answers) {
        int[] answer = {};
        int supo1 = 0;
        int supo2 = 0;
        int supo3 = 0;
        int[] supo3sAnswer = {3,3,1,1,2,2,4,4,5,5};
        int max = 0;
        int[] supoScore = new int[3];
        int supo2Cnt = 1;

        for(int i=0; i<answers.length; i++){
            //수포자1
            if(answers[i] == (i%5)+1){
                supo1++;
            }
            //수포자2
            if(i%2 == 0 && answers[i] == 2){
                supo2++;
            } else if (i%2 != 0 ){

                if(supo2Cnt == 6) supo2Cnt = 1;
                if(answers[i] == supo2Cnt){
                    supo2++;
                }
                if(supo2Cnt == 1){
                    supo2Cnt += 2;
                } else {
                    supo2Cnt ++;
                }
            }
            //수포자3
            if(answers[i] == supo3sAnswer[i%10]){
                supo3++;
            }
        }

        supoScore[0] = supo1;
        supoScore[1] = supo2;
        supoScore[2] = supo3;

        ArrayList<Integer> supoScoreList = new ArrayList<>();
        for(int j=0; j<supoScore.length; j++){
            if(j == 0){
                supoScoreList.add(j+1);
                max = supoScore[j];
            } else if (max == supoScore[j]){
                supoScoreList.add(j+1);
            } else if (max < supoScore[j]){
                supoScoreList.clear();
                supoScoreList.add(j+1);
                max = supoScore[j];
            }
        }

        answer = new int[supoScoreList.size()];
        for(int k=0; k<answer.length; k++){
            answer[k] = supoScoreList.get(k);
        }

        return answer;
    }
}
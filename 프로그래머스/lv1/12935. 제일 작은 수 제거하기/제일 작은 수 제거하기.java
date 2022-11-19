import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        int minNum = 0;

        if(arr.length == 1){
            answer = new int[1];
            answer[0] = -1;
        } else {
            for (int i=0; i<arr.length; i++){
                if(i==0){
                    minNum = arr[i];
                } else {
                    minNum = Math.min(minNum, arr[i]);
                }
            }

            ArrayList<Integer> num_arr = new ArrayList<Integer>();
            for (int j=0; j<arr.length; j++){
                if(arr[j] == minNum){
                    continue;
                } else {
                    num_arr.add(arr[j]);
                }
            }

            answer = new int[num_arr.size()];
            for (int k=0; k<answer.length; k++){
                answer[k] = num_arr.get(k);
            }
        }
        return answer;
    }
}
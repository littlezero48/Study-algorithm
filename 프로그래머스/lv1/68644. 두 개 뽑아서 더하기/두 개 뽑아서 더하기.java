import java.util.ArrayList;

class Solution {
    public int[] solution(int[] numbers) {
        int[] arr = new int[201];
        int[] answer = {};
        int zeroCnt = 0;
        for(int i=0; i<numbers.length; i++){
            if(i == numbers.length){
                break;
            }
            for(int j=i+1; j<numbers.length; j++){
                int idx = numbers[i] + numbers[j];
                if(idx == 0){
                    zeroCnt++;
                } else if (arr[idx] != idx){
                    arr[idx] = idx;
                }
            }
        }

        ArrayList<Integer> arr1 = new ArrayList<>();
        for(int j=0; j<arr.length; j++){
            if(j==0 && zeroCnt != 0){
                arr1.add(0);
                continue;
            }
            if(arr[j] != 0){
                arr1.add(arr[j]);
            }
        }

        answer = new int[arr1.size()];
        for(int k=0; k<answer.length; k++){
            answer[k] = arr1.get(k);
        }
        
        return answer;
    }
}
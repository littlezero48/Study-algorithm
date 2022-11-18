import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> arr1 = new ArrayList<Integer>();

        for(int i=0; i<arr.length; i++){
            if(arr[i]%divisor == 0){
                arr1.add(arr[i]);
            }
        }

        if (arr1.size() == 0){
            arr1.add(-1);
        }
        
        int[] answer = new int [arr1.size()];
        for(int j=0; j<arr1.size(); j++){
            answer[j] = arr1.get(j);
        }

        Arrays.sort(answer);
        
        return answer;
    }
}
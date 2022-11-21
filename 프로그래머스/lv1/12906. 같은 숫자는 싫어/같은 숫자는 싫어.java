import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};

        ArrayList<Integer> arr1 = new ArrayList<Integer>();

        for(int i=0; i<arr.length; i++){
            if(i==0){
                arr1.add(arr[0]);
            } else {
                if(arr[i-1] != arr[i]){
                    arr1.add(arr[i]);
                }
            }
        }

        answer = new int[arr1.size()];
        for(int j=0; j<answer.length; j++){
            answer[j] = arr1.get(j);
        }

        return answer;
    }
}
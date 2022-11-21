import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int []arr) {
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

        return arr1;
    }
}
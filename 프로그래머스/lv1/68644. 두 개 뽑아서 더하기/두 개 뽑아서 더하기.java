import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] numbers) {
        int[] arr = new int[201];
        int[] answer = {};
        int zeroCnt = 0;
        for(int i=0; i<numbers.length; i++){
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
        
        return arr1;
    }
}
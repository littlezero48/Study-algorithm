import java.util.Arrays;

class Solution {
    public long solution(long n) {
      
        long answer = 0;
        
        char[] num_arr = Long.toString(n).toCharArray();       
        Arrays.sort(num_arr);
        
        String merge = "";
        int len = num_arr.length;
        for(int j=0; j<len; j++){
            merge += num_arr[len-j-1];
        }
        
        answer = Long.parseLong(merge);
        return answer;
    }
}
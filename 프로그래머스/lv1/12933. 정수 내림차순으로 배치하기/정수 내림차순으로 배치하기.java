import java.util.ArrayList;
import java.util.Comparator;
class Solution {
    public long solution(long n) {
      
        long answer = 0;
        
        ArrayList<Integer> num_arr = new ArrayList<Integer>();
        
        for(int i=0; 0<n; i++){
            num_arr.add((int) (n%10));
            n /= 10;
        }
        
        num_arr.sort(Comparator.naturalOrder());
        String merge = "";
        int len = num_arr.size();
        for(int j=0; j<len; j++){
            merge += Integer.toString(num_arr.get(len-j-1));
        }
        
        answer = Long.parseLong(merge);
        return answer;
    }
}
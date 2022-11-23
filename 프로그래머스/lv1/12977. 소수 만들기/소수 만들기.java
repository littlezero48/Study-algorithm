import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int solution(int[] nums) {
        int sum = 0;
        int numsLen = nums.length;
        
        // for문을 돌릴 횟수는 nCr로 구한다.
        ArrayList<Integer> sumArr = new ArrayList<>();
        int sumCaseFull = (numsLen*(numsLen-1)*(numsLen-2)) / 6; // 조합 공식 nCr = nPr/r!  // n숫자개수 r선택개수
        for(int i=0; i<numsLen; i++){
            for(int j=i+1; j<numsLen; j++){
                for(int k=j+1; k<numsLen; k++){
                    sumArr.add(nums[i] + nums[j] + nums[k]);
                }
            }
        }

        // 소수를 어떻게 가리나
        int primeNumCnt = 0;
        int numCnt = 0;
        for(int z=0; z<sumArr.size(); z++){
            int sumOne = sumArr.get(z);
            for(int a=2; a<sumOne; a++){
                if(sumOne%a == 0) {
                    numCnt++;
                }
            }
            if(numCnt == 0){
                primeNumCnt++;
            }
            numCnt=0;
        }
        return primeNumCnt;
    }
}
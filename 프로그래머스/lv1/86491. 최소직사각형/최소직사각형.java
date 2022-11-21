class Solution {
    public int solution(int[][] sizes) {
        int longSideMax = 0;
        int shortSideMax = 0;
        
        for(int i=0; i<sizes.length; i++){
            if(sizes[i][0] >= sizes[i][1]) {
                longSideMax = Math.max(longSideMax, sizes[i][0]);
                shortSideMax = Math.max(shortSideMax, sizes[i][1]);
            } else if (sizes[i][0] < sizes[i][1]){
                longSideMax = Math.max(longSideMax, sizes[i][1]);
                shortSideMax = Math.max(shortSideMax, sizes[i][0]);
            } 
        }
        
        return longSideMax * shortSideMax;
    }
}
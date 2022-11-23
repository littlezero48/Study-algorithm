class Solution {
    public String solution(String new_id) {
        String changeID = "";
        int sameCnt = 0;

        new_id = new_id.toLowerCase();  //1단계

        char[] charArr = new_id.toCharArray();
        for (int i = 0; i < charArr.length; i++) {
            // 2단계
            if ((48 <= charArr[i] && 57 >= charArr[i]) || (97 <= charArr[i] && 122 >= charArr[i]) || charArr[i] == '-' || charArr[i] == '_' || charArr[i] == '.') {
                //3단계
                if(changeID.equals("")){
                    changeID += charArr[i];
                } else if(i != 0 && charArr[i] == '.' && changeID.substring(changeID.length()-1).equals(".")){
                    continue;
                } else {
                    changeID += charArr[i];
                }
            } else {
                continue;
            }
        }

        // 4단계
        if(!changeID.equals("")){
            int finalIdx = changeID.length() - 1;
            String startStr = changeID.substring(0,1);
            String EndStr = changeID.substring(changeID.length()-1);
            if (finalIdx == 0 && startStr.equals(".")){
                changeID = "";
            } else if(startStr.equals(".") && EndStr.equals(".")) {
                changeID = changeID.substring(1, finalIdx);
            } else if(startStr.equals(".")){
                changeID = changeID.substring(1);
            } else if(EndStr.equals(".")) {
                changeID = changeID.substring(0,finalIdx);
            }
        }


        // 5단계
        if(changeID.equals("")){
            changeID = "a";
        }

        // 6단계
        if(changeID.length() > 15){
            changeID = changeID.substring(0, 15);
            if(changeID.substring(14).equals(".")){
                changeID = changeID.substring(0,14);
            }
        }

        //7단계
        int changIDLen = changeID.length();
        if(changIDLen <= 2){
            for(int j=0; j<3-changIDLen; j++){
                changeID += changeID.substring(changeID.length()-1);
            }
        }

        return changeID;
    }
}
class Solution {

    static int row;
    static int col;

    public static int findMaxIndex(int currIdx, int depthDce){
        for (int i = 0; i < depthDce; i++){
            currIdx = currIdx * 2 +1;
        }

        return currIdx;
    }

    public int kthGrammar(int n, int k) {
        row = n;
        col = k;
        return backTrack(0, 1, 0);
    }

    public static int backTrack(int value, int depth, int column){
        int result;
        if (depth == row) return value;
        
        // go right
        if (findMaxIndex(column*2, row - depth -1) < col-1){
            result = value == 0? backTrack(1, depth+1, column*2+1) : backTrack(0, depth+1, column*2+1);
        } else {
            // go left
            result = value == 0? backTrack(0, depth+1, column*2) : backTrack(1, depth+1, column*2);
        }
        return result;
    }
}

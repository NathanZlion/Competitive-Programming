class Solution {

    static int row;
    static int col;

    public static int findMaxIndex(int currIdx, int depthDce){
        for (int i = 0; i < depthDce; i++){
            currIdx *= 2;
            currIdx += 1;
        }
        return currIdx;
    }

    public int kthGrammar(int n, int k) {
        row = n;
        col = k;
        return backTrack(0, 1, 0);
    }

    public static int backTrack(int value, int depth, int column){

        if (depth == row){
            return value;
        }

        if (findMaxIndex(column*2, row - depth -1) < col-1){
            // go right
            if (value == 0)
                return backTrack(1, depth+1, column*2+1);

            return backTrack(0, depth+1, column*2+1);
        }
        
        // else go left
        if (value == 0)
            return backTrack(0, depth+1, column*2);

        return backTrack(1, depth+1, column*2);
    }
}

class Solution {

    public int[] countBits(int n) {

        int[] res = new int[n+1];
        int bitCount;
        int number;

        for (int i = 0; i < n+1; i++){
            bitCount = 0;
            number = i;

            while (number > 0){
                bitCount += number & 1;
                number >>= 1;
            }
            
            res[i] = bitCount;
        }

        return res;
    }
}
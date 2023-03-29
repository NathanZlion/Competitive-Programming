class Solution {
    Map<Integer, Integer> memo;

    public int countOnes(int number){
        
        int bitCount = 0;
        while (number > 0){
            bitCount += number & 1;
            number >>= 1;
        }
        
        return bitCount;
    }

    public int[] countBits(int n) {

        int[] res = new int[n+1];

        for (int i = 0; i < n+1; i++){
            res[i] = countOnes(i);
        }

        return res;
    }
}
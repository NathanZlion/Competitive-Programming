class Solution {
    public int countOnes(int number){
        int onesCount = 0;

        while (number > 0){
            onesCount += (number%2);
            number /= 2;
        }
        return onesCount;
    }

    public int[] countBits(int n) {
        int[] res = new int[n+1];

        for (int i = 0; i < n+1; i++){
            res[i] = countOnes(i);
        }

        return res;
    }
}
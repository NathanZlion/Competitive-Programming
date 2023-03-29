class Solution {
    Map<Integer, Integer> memo;

    public int countOnes(int number){
        if (memo.containsKey(number)) return memo.get(number);

        if (number % 2 == 0) return countOnes(number/2);

        return 1 + countOnes(number/2);
    }

    public int[] countBits(int n) {
        
        this.memo = new HashMap();
        memo.put(0,0);
        memo.put(1,1);

        int[] res = new int[n+1];

        for (int i = 0; i < n+1; i++){
            memo.put(i, countOnes(i));
            res[i] = memo.get(i);
        }

        return res;
    }
}
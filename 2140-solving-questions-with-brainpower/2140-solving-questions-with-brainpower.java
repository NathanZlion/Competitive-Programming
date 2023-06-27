class Solution {
    // a hash map to store previosly calculated most points for indices
    Map<Integer, Long> memo = new HashMap();
    int[][] question;

    public long mostPointsForIndex(Integer index){

        // already precalculated value
        if (memo.containsKey(index)) {
            return memo.get(index);
        }
        
        // the base case
        if (index >= question.length){
            return 0;
        }

        long mostPointIfSolved = question[index][0] + mostPointsForIndex(index + question[index][1] + 1);
        long mostPointIfSkipped = mostPointsForIndex(index + 1);

        memo.put(index, Math.max(mostPointIfSolved, mostPointIfSkipped));

        return memo.get(index);
    }
    
    public long mostPoints(int[][] questions) {
        question = questions;
        return mostPointsForIndex(0);
    }
}
class Solution {
    int minimum_fairness = Integer.MAX_VALUE;
    private int[] children_cookies;
    private int[] cookies_bag;
    int num_of_children;

    public static int fairness(int[] arr){
        int fairness_ = arr[0];
        
        for (int index = 1; index < arr.length; index++){
            if (arr[index] > fairness_){
                fairness_ = arr[index];
            }
        }
        return fairness_;
    }

    public void backTrack(int index){
        int curr_fairness = fairness(children_cookies);
        
        if (curr_fairness >= minimum_fairness){
            return ;
        }
        
        if (index == cookies_bag.length){
            minimum_fairness = Math.min(curr_fairness, minimum_fairness);
            return ;
        }
        
        for (int i =0; i < num_of_children; i++){
            children_cookies[i] += cookies_bag[index];
            backTrack(index+1);
            children_cookies[i] -= cookies_bag[index];            
        }
    }

    public int distributeCookies(int[] cookies, int k) {
        children_cookies = new int[k];
        cookies_bag = cookies;
        num_of_children = k;
        backTrack(0);

        return minimum_fairness;
    }
}

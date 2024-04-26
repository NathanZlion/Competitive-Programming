func twoSum(nums []int, target int) []int {
    
    var hashmap = map[int]int {};

    for i := 0; i < len(nums); i++ {
        value, ok := hashmap[target - nums[i]];
        
        if ok {
            return []int {value, i};
        }
        
        hashmap[nums[i]] = i;
    }
    return []int {};
}

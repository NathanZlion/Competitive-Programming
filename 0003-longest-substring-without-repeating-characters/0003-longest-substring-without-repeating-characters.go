func max(a, b int) int {
    if a > b {
        return a;
    } else {
        return b;
    }
}

func lengthOfLongestSubstring(s string) int {
    var left int = 0;
    var counter = map[byte]int {}; // a map from value to frequency
    var maxSubstringLength int = 0;

    for right := 0; right < len(s); right++ {
        // increment counter
        counter[s[right]] ++;

        for counter[s[right]] > 1 {
            counter[s[left]] --;
            left ++;
        }
        maxSubstringLength = max(maxSubstringLength, right - left + 1);
    }
    return maxSubstringLength;
}

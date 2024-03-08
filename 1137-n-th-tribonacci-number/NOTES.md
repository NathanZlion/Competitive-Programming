​I can actually do this in 0(n) space with simple dp. I hold an array of all the dp calculated
where the index represents the ith, and the values are the tribonacci values calculated.

Since after calculating the ith tribonacci the i - 3rd eleement is actually not needed. So I came up with an approach that uses 0(1) space is to use a deque to remove the elemenet from the beginning og the queue after calculating each value.

# 322. Coin Change
- dp, bottom up approach
​
## Intuition
The dp array is used to store precalculated values. The index of the dp array represents the amount of coin and the value at dp[index] is the minimum number of coins needed to make that amount (index).
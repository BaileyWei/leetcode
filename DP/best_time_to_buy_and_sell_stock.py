"""
股票问题，考虑三个因素:
1. 第几天
2. 最高交易上限几次
3. 手中股票状态，持有/不持有/冷冻期


base case：
dp[-1][...][0] = dp[...][0][0] = 0
dp[-1][...][1] = dp[...][0][1] = -infinity

状态转移方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
"""

# 121
# 简化版，只买卖一次，只依赖前一次的结果，所以可以简化为两个变量存储
class Solution:
    def maxProfit(self, prices) -> int:
        dp_0, dp_1 = 0, -prices[0]
        for i,price in enumerate(prices[1:]):
            dp_0 = max(dp_1+price, dp_0)
            dp_1 = max(dp_1, -price)
        return dp_0

# 122
# 买卖次数不限
class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
        return dp[-1][0]

class Solution:
    def maxProfit(self, prices) -> int:
        dp_0 = 0
        dp_1 = -prices[0]
        for i in range(1, len(prices)):
            # 和121唯一不同的就是因为无限次买卖所以在买入下一轮之前上一轮是有利润的，121中temp恒为0
            temp = dp_0
            dp_0 = max(dp_0, dp_1+prices[i])
            dp_1 = max(temp-prices[i], dp_1)
        return dp_0
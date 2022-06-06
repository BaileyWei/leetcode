"""
https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%9B%A2%E7%81%AD%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98.md

股票问题，考虑三个因素:
1. 第几天
2. 最高交易上限几次
3. 手中股票状态，持有/不持有


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

# 122使用贪心算法会更高效
# 因为不限制买卖次数，凡是当前价格比前一天高，就可以在前一天买入今天卖出
class Solution:
    def maxProfit(self, prices) -> int:
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res


# 123 多了交易次数的限制，需要穷举交易次数
class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[[0,0] for _ in range(3)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(1,3):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        return dp[-1][2][0]
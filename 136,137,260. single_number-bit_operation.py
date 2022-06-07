"""
位运算：
https://www.runoob.com/w3cnote/bit-operation.html

异或运算:
参加运算的两个数据，按二进制位进行“异或”运算。
运算规则：0^0=0；   0^1=1；   1^0=1；   1^1=0；
即：参加运算的两个对象，如果两个相应位为“异”（值不同），则该位结果为1，否则为0。
特殊, 0和任何数字异或为当前数字

与运算:
参加运算的两个数据，按二进制位进行“与”运算。
运算规则：0&0=0;   0&1=0;    1&0=0;     1&1=1;
即：两位同时为“1”，结果才为“1”，否则为0

a & (-a) 可以获得a最低的非0位 比如a的二进制原码是 0000 1010，这里最低非0位是bit 1（从右往左第2位）
-a在二进制中的表示是补码(2's complement code)形式，即先按位取反再加1
取反得 1111 0101(即1's complement code，反码)
加1得 1111 0110(即2's complement code，补码)
原码(0000 1010) 与 补码(1111 0110) 做与运算(&)，得 0000 0010，即原码 0000 1010的LSB

### 更详细的解释： 我们从右向左看发生了什么：
原码最低非0位右边所有的0，经由取反后全部变为1，反码+1会导致这些1逐位发生进位并变为0，最终进位记到最低非0位
原最低非0位是1，取反后是0，进位到这一位0变成1，不再向左进位
原最低非0位左边的每一位经由取反后 和 原码 进行与运算必为0
"""


# 136
class Solution:
    def singleNumber(self, nums):
        _sum = 0
        for num in nums:
            _sum ^= num
        return _sum


# 260
class Solution:
    def singleNumber(self, nums):
        _sum = 0
        for num in nums:
            _sum ^= num
        # 找到最后一个二进制位为1的数字，表示两个数字在这一位不同
        lowb = _sum & (-_sum)

        num1, num2 = 0, 0
        # 通过与操作判断lowb位是否为1，来分流nums变成两个子数组，分别做异或，得到两个不一样的数字
        # 与运算,1只有和1与才不为0，0和什么与都为0
        # lowb除了最低二进制位为1其他位都为0，也就是其他位无论为什么最终都是0，只有最低二进制位为1的时候整个数字不为0，这是最快区分的方法
        for num in nums:
            if num & lowb == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


# 137
# 考虑数字的二进制形式，对于出现三次的数字，各 二进制位 出现的次数都是 3 的倍数。
# 因此，统计所有数字的各二进制位中 1 的出现次数，并对 3 求余，结果则为只出现一次的数字。

# 使用两位二进制数字来扫描每一个数字的第i位（计算时实际上是同时扫描所有位）
# https://leetcode.cn/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/
class Solution:
    def singleNumber(self, nums) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

if  __name__ == '__main__':
    Solution().singleNumber([1,2,1,3,2,5])
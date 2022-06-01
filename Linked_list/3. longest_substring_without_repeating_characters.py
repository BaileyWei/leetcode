# 双指针


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        c_dict = {s[0]: 0}
        max_length = 1
        l, r = 0, 1
        while r < len(s):
            if s[r] not in s[l:r]:
                max_length = max(max_length, r - l + 1)
                c_dict[s[r]] = r
            else:
                # 先取index 再更新index
                l = c_dict[s[r]] + 1
                c_dict[s[r]] = r
            r = r + 1
        return max_length


if __name__ == '__main__':
    Solution().lengthOfLongestSubstring("aa")
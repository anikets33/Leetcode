class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [nums[0]]
        suf = [nums[-1]]
        for i in range(1, n):
            if pre[i-1] != 0:
                pre.append(nums[i] * pre[i-1])
            else:
                pre.append(nums[i])
            if suf[i-1] != 0:
                suf.append(nums[n-1-i] * suf[i-1])
            else:
                suf.append(nums[n-1-i])
        #print(pre, suf)
        return max(max(pre), max(suf))

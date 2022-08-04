class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [arr[0]]
        for i in range(1, n):
            prefix.append(prefix[i-1] + arr[i])
            
        pre = [prefix[-1]]
        for i in range(1, n):
            pre.append(pre[i-1] + prefix[n-1-i])
                
        k, s = 1, 0
        while k <= n:
            s += pre[k-1] - (pre[-1] - pre[n-k])
            k += 2
            
        return s

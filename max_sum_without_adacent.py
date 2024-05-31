class Solution:
    # @param A : list of list of integers
    # @return an integer
    def max_sum_without_adacent(self, arr, n):
        dp = [-1] * n

        def max_sum(idx, dp):
            if idx >= n:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            dp[idx] = max(max_sum(idx+1, dp), arr[idx] + max_sum(idx+2, dp))
            return dp[idx]
        return max_sum(0, dp)

    def adjacent(self, A):
        n = len(A[0])
        new_arr = []
        for i in range(n):
            new_arr.append(max(A[0][i], A[1][i]))

        return self.max_sum_without_adacent(new_arr, len(new_arr))



def longest_palindromic_subseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j]:
                if l == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]



print(longest_palindromic_subseq("BBABCBCAB"))

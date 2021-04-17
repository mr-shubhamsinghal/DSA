
"""
FLOW007
"""


T = int(input())
if T >= 1 or T <= 1000:
    for _ in range(T):

        n = int(input())
        if n < 1 or n > 1000000:
            continue
        a = list(str(n))
        ans = ''
        for i in range(len(a)):
            ans += a.pop()
        print(int(ans))

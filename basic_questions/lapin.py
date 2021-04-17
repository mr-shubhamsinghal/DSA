"""
Lapindromes
"""

n = int(input())

for _ in range(n):
    s = input()
    s_len = len(s)
    if s_len < 2 and s_len > 1000:
        break

    larr = []
    rarr = []

    for _ in range(26):
        larr.append(0)
        rarr.append(0)

    for i in range(0, s_len//2):
        c = s[i]
        larr[ord(c) - ord('a')] += 1

    # s_len = 4 -----> 2 to s_len
    # s_len = 5 -----> 3 to s_len
    # s_len = 6 -----> 3 to s_len
    # s_len = 7 -----> 4 to s_len
    for j in range((s_len + 1)//2, s_len):
        c = s[j]
        rarr[ord(c) - ord('a')] += 1

    is_same = True
    for i in range(26):
        if larr[i] != rarr[i]:
            is_same = False
            break

    if is_same:
        print('YES')
    else:
        print('NO')

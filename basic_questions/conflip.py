
"""
CONFLIP
"""

T = int(input())

if T > 0 and T <= 10:

    for _ in range(T):

        G = int(input())

        if G < 1 or G > 20000:
            continue

        for i in range(G):

            I, N, Q = map(int, input().split())

            if (N < 1 or N > 10) and (I < 1 or I > 2) and (Q < 1 or Q > 2):
                continue
        
            if I == Q:
                print(N//2)
            else:
                if N%2 == 0:
                    print(N//2)
                else:
                    print(N//2 + 1)

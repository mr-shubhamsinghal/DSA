
"""
MULTHREE
https://www.youtube.com/watch?v=1p6Xod8Bgl0&t=3287s
1:50:00 to 2:40:00
"""

T = int(input())
for _ in range(T):

    k, d0, d1 = map(int, input().split())
    last_d = (d0 + d1)%10
    total = d0 + d1 + last_d

    if k == 2:
        if (d0*10 + d1)%3 == 0:
            print('YES')
        else:
            print('NO')
        continue

    rem_digit = k - 3

    while rem_digit > 0:
        
        if last_d == 6:
            sets = rem_digit//4
            total += 20 * sets

            rem_digit -= sets*4
            if rem_digit == 0:
                break
            elif rem_digit == 1:
                total += 2
            elif rem_digit == 2:
                total += 6
            elif rem_digit == 3:
                total += 14
            rem_digit = 0
            break

        elif last_d == 0:
            break
        else:
            last_d = (last_d * 2) % 10
            total += last_d
            rem_digit -= 1


    if total % 3 == 0:
        print('YES')
    else:
        print('NO')


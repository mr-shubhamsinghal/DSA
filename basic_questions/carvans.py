
"""
carvans
"""

T = int(input())
for _ in range(T):
    n = int(input())
    cars = list(map(int, input().split(' ')))
    ans = 0

    ahead_car_speed = cars[ans]
    for i in range(n):
        if ahead_car_speed >= cars[i]:
            ans += 1
            ahead_car_speed = cars[i]
    print(ans)

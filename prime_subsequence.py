
def isPrime(num):
    
    if num < 2:
        return False

    i = 2
    while i*i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def solve(arr):
    
    count = 0
    for num in arr:
        if isPrime(num):
            count += 1

    return ((2 ** count) - 1) % (10 ** 9 + 7)


if __name__ == "__main__":
    # arr = list(map(int, input().split()))
    arr = [9, 4, 9, 1, 5]
    ans = solve(arr)
    print(ans)

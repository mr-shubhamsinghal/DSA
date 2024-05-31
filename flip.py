
def solve(arr):
    
    l = 0
    r = 0
    csum = []
    msum = 0

    if arr[0] == '0':
        csum.append(1)
    else:
        csum.append(0)
    
    msum = csum[0]

    for i in range(1, len(arr)):
        if arr[i] == '1':
            if csum[i-1] == 0:
                csum.append(0)
            else:
                csum.append(csum[i-1] - 1)
        else:
            csum.append(csum[i-1] + 1)
        
        if csum[i] > msum:
            msum = csum[i]
            r = i
    
    for i in range(r, -1, -1):
        if csum[i] == 0:
            l = i
            break
    
    if r == 0:
        return []
    
    return [l+2, r+1]

if __name__ == "__main__":
    # arr = '11000011101'
    # arr = '111'
    arr = '010'
    ans = solve(arr)
    print(ans)
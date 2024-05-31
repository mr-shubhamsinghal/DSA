def kadane(A):
    n = len(A)
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(n):
        max_ending_here += A[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

def get_prefix_sum_arr_matrix(A, R, C):

    matrix = [[0] * C for _ in range(R)]
    for c in range(C):
        matrix[0][c] = A[0][c]
        for r in range(1, R):
            matrix[r][c] = matrix[r-1][c] + A[r][c]
    
    return matrix

def solve(A):
    N = len(A)
    M = len(A[0])
    prefix_sum_arr_matrix = get_prefix_sum_arr_matrix(A, N, M)
    max_sum = float('-inf')
    for i in range(M):
        sum_arr = [0] * N
        for j in range(i, M):
            for r in range(N):
                sum_arr[r] += A[r][j]
            # sum_arr
            
            max_sum_arr = kadane(sum_arr)
            max_sum = max(max_sum_arr, max_sum)

    return max_sum


if __name__ == "__main__":
    # A = [[-83,-73,-70,-61],[-56,-48,-13,4],[38,48,71,71]]
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solve(A))

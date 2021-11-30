# https://www.youtube.com/watch?v=-VpH54mhSu4&list=PL5TJqBvpXQv6TtedyS_a_pJK2uVrksh7D&index=3

def solve(A):
    # [-2, 1, 2, 3, 5, -4]
    min, max = 0, 0
    # min, max = A[0], A[0] Other way to start beginning from the first position

    for value in A:
        if value <= min:
            min = value 
        if value >= max:
            max = value 
    return min + max

A = [-2, 1, 2, 3, 5, -4]
B = [-4, -2, 1, 5, 10, 20, -15]

print(solve(A))
print(solve(B))
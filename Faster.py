# Option:2 Longest Cubic Subsequence
from itertools import combinations


def lec_length(A, B, C):
    la  = len(A)
    lb = len(B)
    lc = len(C)

    dp = [[0] * (lc + 1) for _ in range(la + 1) for _ in range(lb + 1)]

    for a in range(1, la + 1):
        for b in range(1, lb + 1):
            for c in range(1, lc + 1):

                if A[a-1] == B[b-1] == C[c-1]:
                    dp[a][b][c] = (dp[a-1][b-1][c-1] + 1)
                else:
                    dp[a][b][c] = max(dp[a-1][b][c], dp[a][b-1][c], dp[a][b][c-1])
    return dp[la][lb][lc]



def is_cubic(squence):
    n = len(squence)

    if n % 3 != 0:
        return False

    k = n // 3

    first = squence[:k]
    second = squence[k:2*k]
    third = squence[2*k:]

    return first == second == third

def lognest_sub_squares(sequence):
    n = len(sequence)
    for length in range(n - n % 3, 0, -3):
        for i in combinations(range(n), length):
            solution = "".join(sequence[index] for index in i)
            if is_cubic(solution):
                return solution
    return ""


def main():


    sequence = "atcgtatgcatgca"

    result = lognest_sub_squares(sequence)

    print("input:", sequence)
    print("output:", result)
    print("length:", len(result))

main()
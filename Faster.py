# Option:2 Longest Cubic Subsequence
from itertools import combinations


def lcs_length(A, B, C):
    la  = len(A)
    lb = len(B)
    lc = len(C)

    prev = [[0] * (lc + 1) for _ in range(la + 1) for _ in range(lb + 1)]

    for a in range(1, len(A) + 1):
        cur = [[0] * (lc + 1) for _ in range(lb + 1)]
        x = A[a-1]

        for b in range(1, lc + 1):
            y = B[b-1]

            for c in range(1, lc + 1):
                if x == y == C[c-1]:
                    cur[b][c] = prev[b-1][c-1] + 1
                else:
                    cur[b][c] = max(prev[b][c],  cur[b-1][c], cur[b][c-1])
        prev = cur
    return prev[lb][lc]

def longest_cubic_subsequence(sequence):
    n = len(sequence)
    best_len = 0
    best_cut = (0, 0)
    for i in range(n+1):
        for j in range(i, n+1):
            A = sequence[:i]
            B = sequence[i:j]
            C = sequence[j:]

            k = lcs_length(A, B, C)
            if k > best_len:
                best_len = k
                best_cut = (i, j)
    return 3 * best_len, best_cut

def longest_cubic_subsequence(sequence):
    n = len(sequence)
    best = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            A = sequence[:i]
            B = sequence[i:j]
            C = sequence[j:]

            k = lcs_length(A, B, C)
            best = max(best, k)
    return 3*best



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
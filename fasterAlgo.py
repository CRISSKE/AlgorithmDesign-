# Option:2 Longest Cubic Subsequence
from itertools import combinations


def lcs_length(A, B, C):
    la  = len(A)
    lb = len(B)
    lc = len(C)

    # Initialize prev dp layer
    prev = []

    for b in range(lb + 1):
        row = [0] * (lc + 1)
        prev.append(row)

    for a in range(1, la + 1):
        # Initialize cur dp layer
        cur = []

        for b in range(lb + 1):
            row = [0] * (lc + 1)
            cur.append(row)

        x = A[a-1]

        for b in range(1, lb + 1):
            y = B[b-1]

            for c in range(1, lc + 1):
                if x == y == C[c-1]:
                    cur[b][c] = prev[b-1][c-1] + 1
                else:
                    cur[b][c] = max(prev[b][c], cur[b-1][c], cur[b][c-1])
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
    i, j = best_cut

    X = lcs_string(sequence[:i], sequence[i:j], sequence[j:])

    return X * 3, best_cut

def lcs_string(A, B, C):
    la = len(A)
    lb = len(B)
    lc = len(C)

    dp = []

    # create dp table
    for a in range(la + 1):
        table = []
        for b in range(lb + 1):
            row = []
            for c in range(lc + 1):
                row.append(0)
            table.append(row)
        dp.append(table)

    # fill the dp table
    for a in range(1, la + 1):
        for b in range(1, lb + 1):
            for c in range(1, lc + 1):

                if A[a-1] == B[b-1] == C[c-1]:
                    dp[a][b][c] = dp[a-1][b-1][c-1] + 1
                else:
                    dp[a][b][c] = max(dp[a-1][b][c], dp[a][b-1][c], dp[a][b][c-1])

    # backtracking to reconstruct the LCS
    result = []
    a = la
    b = lb
    c = lc

    while a>0 and b>0 and c>0:
        if A[a-1] == B[b-1] == C[c-1]:
            result.append(A[a-1])
            a -= 1
            b -= 1
            c -= 1
        elif dp[a][b][c] == dp[a-1][b][c]:
            a -= 1
        elif dp[a][b][c] == dp[a][b-1][c]:
            b -= 1
        else:
            c -= 1
    result.reverse()
    return "".join(result)



def main():


    sequence = "atcgtatgcatgca"

    result, best_cut = longest_cubic_subsequence(sequence)

    print("input:", sequence)
    print("output:", result)
    print("length:", len(result))
    print("best_cut:", best_cut)


if __name__ == "__main__":
    main()
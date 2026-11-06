# Option:2 Longest Cubic Subsequence
from itertools import combinations


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
    sequence = "abcabcabc"

    print("intput:", sequence)
    print("output:", is_cubic(sequence))

main() 
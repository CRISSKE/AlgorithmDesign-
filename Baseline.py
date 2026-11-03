# Option:2 Longest Cubic Subsequence
def is_cubic(squence):
    n = len(squence)

    if n % 3 != 0:
        return False

    k = n // 3

    first = squence[:k]
    second = squence[k:2*k]
    third = squence[2*k:]

    return first == second == third

def main():
    sequence = "abcabcabc"

    print("intput:", sequence)
    print("output:", is_cubic(sequence))

main()
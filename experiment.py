
import time
import random
import statistics

from baseline import lognest_sub_squares
from fasterAlgo import longest_cubic_subsequence


# Experimental settings
SIZES = [6, 9, 12, 15, 18, 21, 24, 27, 30]
TRIALS = 5


def measure_time(algorithm, sequence):
    start = time.perf_counter()
    result = algorithm(sequence)
    elapsed = time.perf_counter() - start

    return result, elapsed


def main():
    rng = random.Random(360)

    print("Input Size | Baseline (s) | Faster (s)")
    print("--------------------------------------")

    for n in SIZES:
        baseline_times = []
        faster_times = []

        for trial in range(TRIALS):

            # Generate a random string
            sequence = ""

            for i in range(n):
                sequence += rng.choice("ACGT")

            # Run Baseline
            baseline_result, t1 = measure_time(
                lognest_sub_squares, sequence
            )

            # Run Faster Algorithm
            faster_output, t2 = measure_time(
                longest_cubic_subsequence, sequence
            )

            faster_result, best_cut = faster_output

            # Verify that both algorithms return
            # the same optimal length
            assert len(baseline_result) == len(faster_result)

            baseline_times.append(t1)
            faster_times.append(t2)

        # Calculate average running time
        baseline_avg = statistics.mean(baseline_times)
        faster_avg = statistics.mean(faster_times)

        print(
            f"n={n} | "
            f"Baseline={baseline_avg:.6f}s | "
            f"Faster={faster_avg:.6f}s"
        )


if __name__ == "__main__":
    main()

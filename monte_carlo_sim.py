import random
from collections import Counter

def simulate_opening_hands(
    deck_size: int = 100,
    land_count: int = 35,
    hand_size: int = 7,
    trials: int = 100_000,
    seed: int | None = None,
) -> Counter:
    """
    Monte Carlo simulator for opening hands.
    Returns a Counter mapping {lands_in_hand: occurrences}.
    """
    if not (0 <= land_count <= deck_size):
        raise ValueError("land_count must be between 0 and deck_size")
    if not (0 <= hand_size <= 7):
        raise ValueError("hand_size must be between 0 and 7")
    if trials <= 0:
        raise ValueError("trials must be positive")

    rng = random.Random(seed)

    # Represent deck as 1 = land, 0 = nonland
    deck = [1] * land_count + [0] * (deck_size - land_count) # deck is a list of 1s and 0s

    counts = Counter()
    for _ in range(trials):
        hand = rng.sample(deck, hand_size)   # sample of deck list
        lands = sum(hand) #sum 1s in sample list to get all lands in sample
        counts[lands] += 1 #add outcome of the run to the result

    return counts

def print_results(counts, trials, hand_size=7):
    print(f"Trials: {trials:,}\n")
    print("Lands | Count     | Percent | Cumulative %")
    print("-" * 46)

    cumulative = 0
    for k in range(0, hand_size + 1):
        count = counts.get(k, 0)
        percent = 100.0 * count / trials
        cumulative += percent

        print(
            f"{k:>5} | "
            f"{count:>9,} | "
            f"{percent:>7.2f}% | "
            f"{cumulative:>11.2f}%"
        )

if __name__ == "__main__":
    TRIALS = 1_000_000
    for landcount in range(32, 39, 1):
        counts = simulate_opening_hands(deck_size=100, land_count=landcount, hand_size=7, trials=TRIALS, seed=42)
        print(f"\nDeck with {landcount} lands:")
        print_results(counts, TRIALS, hand_size=7)
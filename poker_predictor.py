from poker_utils import calculate_best_hand, priority_hand_name


def get_retain_combinations(some_hand, r):
    from itertools import combinations
    return combinations(some_hand, r)


def calculate_best_outcome(some_hand, some_deck):
    best_hand = 1
    n = len(some_hand)
    for r in range(n + 1):
        # combinations of cards that can be replaced, nCr
        # can @JIT the combinations calculation
        retain_combination = get_retain_combinations(some_hand, n - r)
        hand_values = [calculate_best_hand(list(combination) + some_deck[:r]) for combination in retain_combination]
        best_hand = max(max(hand_values), best_hand)

    return priority_hand_name[best_hand]

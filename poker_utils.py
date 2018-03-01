from card_utils import card_order_dict, get_rank_counts, get_suit

priority_hand_name = {
    9: "straight-flush", 8: "four-of-a-kind", 7: "full-house", 6: "flush", 5: "straight", 4: "three-of-a-kind",
    3: "two-pairs", 2: "one-pair", 1: "highest-card"
}

hand_priority = {value: key for key, value in priority_hand_name.items()}


def straight_flush(some_hand):
    return is_flush(some_hand), is_straight(some_hand)


def is_full_house(some_hand):
    return sorted(get_rank_counts(some_hand, values_only=True)) == [2, 3]


def is_flush(some_hand):
    # this can be done in a short circuit manner with an accumulator
    suits = [get_suit(card) for card in some_hand]
    return len(set(suits)) == 1


def is_straight(some_hand):
    value_counts = get_rank_counts(some_hand)
    rank_values = [card_order_dict[i] for i in value_counts.keys()]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):
        return True
    # check for a straight with cyclic Ace
    return set(value_counts.keys()) == {"A", "2", "3", "4", "5"}


def is_two_pairs(some_hand):
    return sorted(get_rank_counts(some_hand, values_only=True)) == [1, 2, 2]


def is_n_of_a_kind(some_hand, n):
    return n in get_rank_counts(some_hand, values_only=True)


# as you can see refactoring the methods to all come from a single method
# would sacrifice readability to an extent
# Not overusing DRY since the repetition is limited to 2


def calculate_best_hand(some_hand):
    # get flush and straight details here, so I don't have to calculate again
    is_a_flush, is_a_straight = straight_flush(some_hand)
    # running them in sequence seems better since it's a short circuit
    if is_a_straight and is_a_flush:
        return hand_priority['straight-flush']
    if is_n_of_a_kind(some_hand, 4):
        return hand_priority['four-of-a-kind']
    if is_full_house(some_hand):
        return hand_priority['full-house']
    if is_a_flush:
        return hand_priority['flush']
    if is_a_straight:
        return hand_priority['straight']
    if is_n_of_a_kind(some_hand, 3):
        return hand_priority['three-of-a-kind']
    if is_two_pairs(some_hand):
        return hand_priority['two-pairs']
    if is_n_of_a_kind(some_hand, 2):
        return hand_priority['one-pair']
    return hand_priority['highest-card']

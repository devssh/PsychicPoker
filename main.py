from itertools import combinations
from collections import Counter
from itertools import chain

# since I am doing it in Python which is not strongly typed, I'll use functions instead of classes
# if it were Java I would've used classes nicely with the Design principles

card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}

priority_hand_name = {
    9: "straight-flush", 8: "four-of-a-kind", 7: "full-house", 6: "flush", 5: "straight", 4: "three-of-a-kind",
    3: "two-pairs", 2: "one-pair", 1: "highest-card"
}

hand_priority = {value: key for key, value in priority_hand_name.items()}


def get_rank_counts(some_hand, values_only=False):
    # since this is a core logic can Just In Time this
    rank_count_dict = dict(Counter(chain.from_iterable(card[0] for card in some_hand)))
    if values_only:
        return rank_count_dict.values()
    return rank_count_dict


def straight_flush(some_hand):
    return is_flush(some_hand), is_straight(some_hand)


def is_full_house(some_hand):
    return sorted(get_rank_counts(some_hand, values_only=True)) == [2, 3]


def is_flush(some_hand):
    # this can be done in a short circuit manner with an accumulator
    suits = [card[1] for card in some_hand]
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


# as you can see I can refactor the methods to all come from a single method
# but that would sacrifice readability to an extent
# I'm gonna stick with not overusing DRY since the repetition is limited to 2


def calculate_best_hand(some_hand):
    # get flush and straight details here, so I don't have to calculate again
    is_a_flush, is_a_straight = straight_flush(some_hand)
    # running them in sequence seems ok since it's a short circuit
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


def predict(some_hand, some_deck):
    best_hand = 1
    n = len(some_hand)
    for r in range(n + 1):
        # combinations of cards that can be replaced, nCr
        # can @JIT the combinations calculation
        retain_combination = combinations(some_hand, n - r)
        for combination in retain_combination:
            possible_hand = list(combination) + some_deck[:r]
            hand_value = calculate_best_hand(possible_hand)
            if hand_value > best_hand:
                best_hand = hand_value

    return priority_hand_name[best_hand]


if __name__ == '__main__':
    count = int(input('Enter number of input lines/trials\n'))
    for _ in range(count):
        data = input('Enter the input of 5 cards in hand and top 5 cards of deck\n').strip()
        # data = [
        #     'TH JH QC QD QS QH KH AH 2S 6S',
        #     '2H 2S 3H 3S 3C 2D 3D 6C 9C TH',
        #     '2H 2S 3H 3S 3C 2D 9C 3D 6C TH',
        #     '2H AD 5H AC 7H AH 6H 9H 4H 3C',
        #     'AC 2D 9C 3S KD 5S 4D KS AS 4C',
        #     'KS AH 2H 3C 4H KC 2C TC 2D AS',
        #     'AH 2C 9S AD 3C QH KS JS JD KD',
        #     '6C 9C 8C 2D 7C 2H TC 4C 9S AH',
        #     '3D 5S 2H QD TD 6S KH 9H AD QH'
        # ]
        assert ' ' in data
        assert len(data) == 29
        cards = data.split(' ')
        assert len(cards) == 10
        card_len = 5
        hand = cards[:card_len]
        deck = cards[card_len:]
        print("Hand:", " ".join(hand), "Deck:", " ".join(deck), "Best hand:", predict(hand, deck))

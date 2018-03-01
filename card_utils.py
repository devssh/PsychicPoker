card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}

suit_set = {'H', 'S', 'D', 'C'}


def get_rank(some_card):
    return some_card[0]


def get_suit(some_card):
    return some_card[1]


def get_rank_counts(some_hand, values_only=False):
    # returns key value mappings of ranks and their counts
    from collections import Counter
    from itertools import chain
    rank_count_dict = dict(Counter(chain.from_iterable(get_rank(card) for card in some_hand)))
    if values_only:
        return rank_count_dict.values()
    return rank_count_dict

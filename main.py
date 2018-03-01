from poker_predictor import calculate_best_outcome

# since I am doing it in Python which is not strongly typed, I'll use functions instead of classes
# if it were Java I would've used classes nicely with the Design principles


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
        print("Hand:", " ".join(hand), "Deck:", " ".join(deck), "Best hand:", calculate_best_outcome(hand, deck))

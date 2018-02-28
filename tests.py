from main import predict

data = [
    'TH JH QC QD QS QH KH AH 2S 6S',
    '2H 2S 3H 3S 3C 2D 3D 6C 9C TH',
    '2H 2S 3H 3S 3C 2D 9C 3D 6C TH',
    '2H AD 5H AC 7H AH 6H 9H 4H 3C',
    'AC 2D 9C 3S KD 5S 4D KS AS 4C',
    'KS AH 2H 3C 4H KC 2C TC 2D AS',
    'AH 2C 9S AD 3C QH KS JS JD KD',
    '6C 9C 8C 2D 7C 2H TC 4C 9S AH',
    '3D 5S 2H QD TD 6S KH 9H AD QH'
]

cards = data[0].split(' ')
assert predict(cards[:5], cards[5:]) == 'straight-flush'

cards = data[1].split(' ')
assert predict(cards[:5], cards[5:]) == 'four-of-a-kind'

cards = data[2].split(' ')
assert predict(cards[:5], cards[5:]) == 'full-house'

cards = data[3].split(' ')
assert predict(cards[:5], cards[5:]) == 'flush'

cards = data[4].split(' ')
assert predict(cards[:5], cards[5:]) == 'straight'

cards = data[5].split(' ')
assert predict(cards[:5], cards[5:]) == 'three-of-a-kind'

cards = data[6].split(' ')
assert predict(cards[:5], cards[5:]) == 'two-pairs'

cards = data[7].split(' ')
assert predict(cards[:5], cards[5:]) == 'one-pair'

cards = data[8].split(' ')
assert predict(cards[:5], cards[5:]) == 'highest-card'

print('All tests passed')

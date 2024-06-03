# This file is used to store common cards

# Important Cards (inconsistent naming but does it really matter?)
club_3 = 0b000000000000010
club_10 = 0b000000100000000
d_jack = 0b010001000000000
q_spades = 0b100010000000000
h_10 = 0b110000100000000

# Team cards
black_king = 0b000100000000000
black_ace = 0b001000000000000
red_king = 0b010100000000000
red_ace = 0b011000000000000

team_cards = [
    black_ace,
    black_king,
    red_ace,
    red_king
]

all_cards = [
    0b000000000000001,
    0b000000000000010,
    0b000000000000100,
    0b000000000001000,
    0b000000000010000,
    0b000000000100000,
    0b000000001000000,
    0b000000010000000,
    0b000000100000000,
    0b000001000000000,
    0b000010000000000,
    0b000100000000000,
    0b001000000000000,
    0b010000000000001,
    0b010000000000010,
    0b010000000000100,
    0b010000000001000,
    0b010000000010000,
    0b010000000100000,
    0b010000001000000,
    0b010000010000000,
    0b010000100000000,
    0b010001000000000,
    0b010010000000000,
    0b010100000000000,
    0b011000000000000,
    0b100000000000001,
    0b100000000000010,
    0b100000000000100,
    0b100000000001000,
    0b100000000010000,
    0b100000000100000,
    0b100000001000000,
    0b100000010000000,
    0b100000100000000,
    0b100001000000000,
    0b100010000000000,
    0b100100000000000,
    0b101000000000000,
    0b110000000000001,
    0b110000000000010,
    0b110000000000100,
    0b110000000001000,
    0b110000000010000,
    0b110000000100000,
    0b110000001000000,
    0b110000010000000,
    0b110000100000000,
    0b110001000000000,
    0b110010000000000,
    0b110100000000000,
    0b111000000000000
]

all_points = {
    0b000000000000001: 0,
    0b000000000000010: 0,
    0b000000000000100: 0,
    0b000000000001000: 0,
    0b000000000010000: 0,
    0b000000000100000: 0,
    0b000000001000000: 0,
    0b000000010000000: 0,
    0b000000100000000: 0,
    0b000001000000000: 0,
    0b000010000000000: 0,
    0b000100000000000: 0,
    0b001000000000000: 0,
    0b010000000000001: 0,
    0b010000000000010: 0,
    0b010000000000100: 0,
    0b010000000001000: 0,
    0b010000000010000: 0,
    0b010000000100000: 0,
    0b010000001000000: 0,
    0b010000010000000: 0,
    0b010000100000000: 0,
    0b010001000000000: -100,
    0b010010000000000: 0,
    0b010100000000000: 0,
    0b011000000000000: 0,
    0b100000000000001: 0,
    0b100000000000010: 0,
    0b100000000000100: 0,
    0b100000000001000: 0,
    0b100000000010000: 0,
    0b100000000100000: 0,
    0b100000001000000: 0,
    0b100000010000000: 0,
    0b100000100000000: 0,
    0b100001000000000: 0,
    0b100010000000000: 100,
    0b100100000000000: 0,
    0b101000000000000: 0,
    0b110000000000001: 0,
    0b110000000000010: 0,
    0b110000000000100: 0,
    0b110000000001000: 10,
    0b110000000010000: 10,
    0b110000000100000: 10,
    0b110000001000000: 10,
    0b110000010000000: 10,
    0b110000100000000: 10,
    0b110001000000000: 20,
    0b110010000000000: 30,
    0b110100000000000: 40,
    0b111000000000000: 50
}

# Arrays
all_clubs = all_cards[:13]
all_diamonds = all_cards[13:26]
all_spades = all_cards[26:39]
all_hearts = all_cards[39:]

# Card mask for stripping suit
card_mask = 0b001111111111111

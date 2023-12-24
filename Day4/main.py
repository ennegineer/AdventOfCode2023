# Scratchcards
# How many of our numbers match the winning numbers on each card?
# The first match is worth 1 point; each after the first doubles the point value of the card.
## How many points do we have total?

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

def find_winners(my_numbers, winning_numbers):
    score = 0
    for number in my_numbers:
        if number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score

game_counter = 0
sum = 0
# Set up the cards
for row in data:
    game_counter += 1
    # Remove the card number
    card = row.split(':')[1]
    # Separate the winning numbers from my numbers
    card = [card.split('|')[0], card.split('|')[1]]
    winning_numbers = list(filter(None, card[0].split(' ')))
    my_numbers = list(filter(None, card[1].split(' ')))
    # Find the score
    score = find_winners(my_numbers, winning_numbers)
    sum += score
print(sum)
    


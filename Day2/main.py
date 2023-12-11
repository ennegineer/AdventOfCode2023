# Cube Conundrum
# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# Part One
# Which games are possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
# Sum the IDs of the possible games.

game_counter = 0
sum = 0
for row in data:
    possible = True
    game_counter += 1
    newrow = row.split(':')[1]
    game = newrow.split(';')
    for item in game:
        red = 0
        blue = 0
        green = 0
        play = item.split(',')
        # print(f'game: {game_counter} | {play}')
        for cubes in play:
            if 'blue' in cubes:
                # isolate the digits
                blue_digits = [int(i) for i in cubes if i.isdigit()]
                blue = int(''.join(map(str, blue_digits)))
            if 'green' in cubes:
                green_digits = [int(i) for i in cubes if i.isdigit()]
                green = int(''.join(map(str, green_digits)))
            if 'red' in cubes:
                red_digits = [int(i) for i in cubes if i.isdigit()]
                red = int(''.join(map(str, red_digits)))
        if red > 12:
            possible = False
            # print(f'red: {red}')
        if green > 13:
            possible = False
            # print(f'green: {green}')
        if blue > 14:
            possible = False
            # print(f'blue: {blue}')

        # print(possible)
    
    if possible == True:
        sum += game_counter
        print(game_counter)
        print(f'sum: {sum}')



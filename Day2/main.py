# Cube Conundrum
# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# Part One
# Which games are possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
# Sum the IDs of the possible games.
def PartOne():
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
            if green > 13:
                possible = False
            if blue > 14:
                possible = False

        if possible == True:
            sum += game_counter
            print(game_counter)
            print(f'sum: {sum}')

# Part Two
# What is the fewest number of cubes of each color per game?
# Multiply these three numbers together for each game.
# What is the sum of these?

def PartTwo():
    sum = 0
    for row in data:
        newrow = row.split(':')[1]
        game = newrow.split(';')
        red = 0
        blue = 0
        green = 0
        for item in game:
            play = item.split(',')
            for cubes in play:
                if 'blue' in cubes:
                    # isolate the digits
                    blue_digits = int(''.join(map(str, [int(i) for i in cubes if i.isdigit()])))
                    if blue == 0 or blue_digits > blue:
                        blue = blue_digits 
                if 'green' in cubes:
                    green_digits = int(''.join(map(str, [int(i) for i in cubes if i.isdigit()])))
                    if green == 0 or green_digits > green:
                        green = green_digits 
                if 'red' in cubes:
                    red_digits = int(''.join(map(str, [int(i) for i in cubes if i.isdigit()])))
                    if red == 0 or red_digits > red:
                        red = red_digits 
        game_min = red * blue * green
        
        sum += game_min
        print(f'sum: {sum}')

PartTwo()
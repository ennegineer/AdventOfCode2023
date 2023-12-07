# Trebuchet!
# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# Part One
# Combine the first digit and last digit from each line to get the two-digit input values.
# Find the total of all the values.

def PartOne(data):
    # Get numbers from string 
    instructions = []
    sum = 0
    for row in data:
        digits = [int(i) for i in row if i.isdigit()]
        instruction = str(digits[0]) + str(digits[-1])
        instructions.append(instruction)
        sum += int(instruction)
    print(sum)
    return sum
    

# Part Two
# First, find any numbers that are spelled out and convert them. Then rerun part one.
def PartTwo():
    pass



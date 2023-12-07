# Trebuchet!
# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# Part One
# Combine the first digit and last digit from each line to get the two-digit input values.
# Find the total of all the values.

def PartOne(input_data):
    # Get numbers from string 
    sum = 0
    for row in input_data:
        digits = [int(i) for i in row if i.isdigit()]
        instruction = str(digits[0]) + str(digits[-1])
        sum += int(instruction)
    print(sum)
    return sum
    

# Part Two
# First, find any numbers that are spelled out and convert them. Then rerun part one.
def search_and_replace():
    with open('input.txt', 'r') as file:
        file_contents = file.read()

        updated_contents = file_contents.replace('eightwo', '82')
        updated_contents = updated_contents.replace('oneight', '18')
        updated_contents = updated_contents.replace('twone', '21')
        updated_contents = updated_contents.replace('one', '1')
        updated_contents = updated_contents.replace('two', '2')
        updated_contents = updated_contents.replace('three', '3')
        updated_contents = updated_contents.replace('four', '4')
        updated_contents = updated_contents.replace('five', '5')
        updated_contents = updated_contents.replace('six', '6')
        updated_contents = updated_contents.replace('seven', '7')
        updated_contents = updated_contents.replace('eight', '8')
        updated_contents = updated_contents.replace('nine', '9')

    with open('new_input.txt', 'w') as file:
        file.write(updated_contents)

search_and_replace()

with open("new_input.txt", "r") as new_input:
    edited_data = new_input.read().split('\n')

PartOne(data)
PartOne(edited_data)

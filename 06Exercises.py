# 6.11. Exercises: Loops
line_start = "<--------------"
line_end = "-------------->"

# 6.11.1. for Practice
print(f"\n{line_start} PART 1 {line_end}")
# a. Print the numbers 0 - 20, one number per line.
print("\n0-20")
for interval in range(21):
    print(interval)

# b. Print only the ODD values from 3 - 29, one number per line.
print("\n3-29 odd")
for odd in range(3, 30, 2):
    print(odd)

# c. Print the EVEN numbers 12 down to -14 in descending order, 
    # one number per line.
print("\n12-(-14) even")
for even in range(12, -15, -2):
    print(even)

# d. Print the numbers 50 down to 20 in descending order, 
    # but only if the numbers are multiples of 3.
print("\n50-20 multiples of 3")
for threes in range(50, 20, -1):
    if threes % 3 == 0:
        print(threes)

print(f"\n{line_start} PART 2 {line_end}")
launch_code = 'LaunchCode'
# Code two for loops to do the following:
    # a. Print out each character of the string, one letter per line. 
        # Do this WITHOUT using index values.
    # b. Now use index values to print each character of the string in reverse order
        # to a new line.
print('\nString chars w/o index values')
for character in launch_code:
    print(character)

print('\nString chars using index values')
string_length = len(launch_code)
for index in range(string_length):
    print(launch_code[index])

print(f"\n{line_start} PART 3 {line_end}")
gibberish = 'Vna#hewzB*rQhT%yq^lv %iPwgOexWo &C^oUoGSdtJLj'
# Print every fifth character, including the first character. 
    # Use index values and range(start, stop, step).
print('\ngibberish fifth chars')
for fifth in range(0, len(gibberish), 5):
    print(gibberish[fifth])

print(f"\n{line_start} BONUS {line_end}")
# a. Replace range(start, stop, step) with range(len(gibberish))
# b. Use an if statement and the modulus (%) operator to check 
    # if the index is divisible by 5.
# c. If True, print the character. If False, do not print the character.
# d. The output should be the same as before.
for fifth in range(len(gibberish)):
    if fifth % 5 == 0:
        print(gibberish[fifth])

# 6.11.2. while Practice
print(f"\n{line_start} PARTS 4-7 {line_end}")
# Define three variables for a spacecraft & assign them an initial value of 0.
    # one for the starting fuel level, 
    # another for the number of astronauts aboard, and 
    # the third for the altitude the spacecraft reaches
fuel_level_start = 0
num_astronauts = 0
altitude = 0

# a. Ask the user for the starting fuel level. 
    # The loop should continue until the user enters a value between 5000 and 30000. 
    # If the user submits a number outside of the range, print "Invalid entry."
# b. Use a second loop to prompt the user for the number of astronauts 
    # (up to a maximum of 7). 
    # Validate the entry by having the loop continue until the user enters an 
    # integer from 1 - 7. For numbers outside of the range, print "Invalid entry."

fuel_level_start = float(input('Enter the starting fuel level: '))
while fuel_level_start < 5000 or fuel_level_start > 30000:
    print('Invalid entry')
    fuel_level_start = float(input())

num_astronauts = int(input('Enter the number of astronauts: '))
while num_astronauts < 1 or num_astronauts > 7:
    print('Invalid entry')
    num_astronauts = int(input())

# Use a third while loop to update the fuel and the altitude of the spacecraft. 
    # Each iteration, decrease the fuel level by 100 units for each astronaut aboard. 
    # Also, increase the altitude by 50 kilometers.
# The loop should end when there is not enough fuel to boost the crew another 50 km, 
    # so the fuel level might not reach 0.
fuel_use = 100 * num_astronauts
while fuel_level_start >= fuel_use:
    fuel_level_start -= fuel_use
    altitude += 50

# After the loops finish, print the result using the phrase, 
    # "The spacecraft gained an altitude of ___ km and has ___ kg of fuel left." 
print(f'The spacecraft gained an altitude of {altitude} km and has {fuel_level_start} kg of fuel left.')

# If the altitude is 2000 km or higher, add "Orbit achieved!" to the output. 
    # Otherwise add, "Failed to reach orbit."

if altitude >= 2000:
    print('Orbit achieved!')
else:
    print('Failed to reach orbit.')

# 6.11.3. The Accumulator Pattern
print(f"\n{line_start} PART 8 {line_end}")
# Use two input statements to prompt the user for a start_value and an end_value. 
    # Both inputs should be integers.
start_value = int(input('Enter a start value: '))
end_value = int(input('Enter an end value: '))

# Use a loop to add up all of the numbers from start_value to end_value. 
    # Use the variable total as the accumulator. 
    # Print "The sum of the numbers from ___ to ___ is ___." 
    # Fill in the blanks with the values for start_value, end_value, and total.
total = 0
if end_value > start_value:
    for value in range(start_value, end_value + 1):
        total += value
else:
    for value in range(end_value, start_value + 1):
        total += value

print(f'\nThe sum of the numbers from {start_value} to {end_value} is {total}.')

print(f"\n{line_start} PART 9 {line_end}")
# Define a variable to hold the string 
    # 'It was a bright cold day in April, and the clocks were striking thirteen.' 
    # Use the accumulator pattern to build a new string. 
    # It should contain all of the characters in the original string, 
    # but without any vowels. For this task, y does NOT count as a vowel. 
    # Print the new string.
string = 'It was a bright cold day in April, and the clocks were striking thirteen.'
new_string = None
vowels = 'aeiou'

for char in string:
    if char.lower() not in vowels:
        if new_string == None:
            new_string = char
        else:
            new_string += char

print(new_string)


print(f"\n{line_start} CHALLENGE {line_end}")
# 6.11.4. Challenge
'''
    If our spacecraft gets hijacked by space pirates, the astronauts can activate 
        a self-destruct sequence to provide some drama for the viewers at home.

    In order to prevent a rogue astronaut from activating the code, 
        it takes two crew members to begin the countdown. 
        Each person must enter a different code, after which the computer will 
        “zip” them together before overloading the engines.

    In a new code file, construct a loop that combines two strings together, 
        alternating the characters from each source. 
        For now, be careful to make both strings the same length.
'''

string_one = 'dsrytesi'
string_two = 'eto h hp'
code = None
for index in range(len(string_one)):
    if code == None:
        code = string_one[index] + string_two[index]
    else:
        code += string_one[index] + string_two[index]

print(code)
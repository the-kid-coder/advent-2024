# This is a problem from the 2024 Advent of Code calendar.
# Part 2 of Day 3

import re

memory_lines = []
dont_pattern = r"don't\(\)"
do_pattern = r"do\(\)"

# The goal of this function is to populate the two lists for this exercise
def input_lines():
    with open("input.txt",'r') as f:
        while True:
            line = f.read().strip()
            if not line:
                break
            
            memory_lines.append(line)

def processProduct(line):
    line_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    number_pattern = r"\d{1,3}"
    total_sum = 0

    products = re.findall(line_pattern, line)
    
    for product in products:
        digits = re.findall(number_pattern, product)
        sum = 1
        for digit in digits:
            sum *= int(digit)
        
        total_sum += sum
    return total_sum

def processDont(line):
    hasDont = 1
    countDont = 0
    return_line = line

    while hasDont is not None:
        countDont += 1
        dont_location = re.search(dont_pattern, return_line)
        dont_start = dont_location.start()

        hasDo = re.search(do_pattern, return_line[dont_start:])
        if hasDo:
            do_start = hasDo.start() + dont_start
            return_line = return_line[0:dont_start] + return_line[do_start:]
        else:
            return_line = return_line[0:dont_start]
        
        hasDont = re.search(dont_pattern, return_line)

    return return_line

# # This function processes the 'dont' and 'do' logic in the line
# def processDont(line):
#     # Case 1: Remove "don't(...)" sections that are followed by "do(...)"
#     line = re.sub(r"don't\(\).*?do\(\)", "", line)
    
#     # Case 2: Remove any "don't(...)" section that doesn't have "do(...)"
#     line = re.sub(r"don't\(\)[^d]*", "", line)
    
#     return line


def main():
    input_lines()
    
    total_sum = 0

    for line in memory_lines:
        hasDont = re.search(dont_pattern, line)
        if hasDont:
            line = processDont(line)

        total_sum += processProduct(line)
    
    print(total_sum)

main()

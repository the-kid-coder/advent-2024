# This is a problem from the 2024 Advent of Code calendar.
# Part 1 of Day 3

import re

memory_lines = []

# The goal of this function is to populate the two lists for this exercise
def input_lines():
    with open("input.txt",'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            
            memory_lines.append(line)

def main():
    input_lines()

    line_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    number_pattern = r"\d{1,3}"
    total_sum = 0

    for line in memory_lines:
        products = re.findall(line_pattern, line)
        for product in products:
            digits = re.findall(number_pattern, product)
            sum = 1
            for digit in digits:
                sum *= int(digit)
            
            total_sum += sum
    
    print(total_sum)

main()

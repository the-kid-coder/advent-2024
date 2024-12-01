# This is a problem from the 2024 Advent of Code calendar.
# Part 1 of Day 1 asked us to find a distance between two lists
# The code below takes as input a file with two lists, and calculates the distance between them
# after sorting the lists in numerical order from smallest to largest
#
# The input file can be found in input.txt

list_left = [] 
list_right = []

# The goal of this function is to populate the two lists for this exercise
def input_lists():
    with open("input.txt",'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            
            row = line.split("   ")
            list_left.append(int(row[0]))
            list_right.append(int(row[1]))

def main():
    input_lists()

    sum = 0
    list_left.sort()
    list_right.sort()

    for i in range(len(list_left)):
        sum += abs(list_left[i] - list_right[i])
    
    print(sum)

main()

# if __name__ == "__main__":
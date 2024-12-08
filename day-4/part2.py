# This is a problem from the 2024 Advent of Code calendar.
# Part 2 of Day 4

maze_lines = []

# The goal of this function is to populate the two lists for this exercise
def input_lines():
    with open("test.txt",'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            
            maze_lines.append(line)

def search_maze():
    mas_found = 0
    rows = len(maze_lines)
    cols = len(maze_lines[0]) if maze_lines else 0

    # Look for center A's (skip edges)
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if maze_lines[row][col] == 'A':  # Found potential center A
                upper_left = maze_lines[row-1][col-1]
                upper_right = maze_lines[row-1][col+1]
                lower_left = maze_lines[row+1][col-1]
                lower_right = maze_lines[row+1][col+1]
                
                if sorted([upper_left, upper_right, lower_left, lower_right]) == ['M', 'M', 'S', 'S'] and upper_left != lower_right:
                    mas_found += 1
    
    return mas_found

def main():
    input_lines()
    print(search_maze())

main()
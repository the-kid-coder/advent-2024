# This is a problem from the 2024 Advent of Code calendar.
# Part 1 of Day 4

maze_lines = []

# The goal of this function is to populate the two lists for this exercise
def input_lines():
    with open("input.txt",'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            
            maze_lines.append(line)

def search_maze():
    xmas_found = 0
    rows = len(maze_lines)
    cols = len(maze_lines[0]) if maze_lines else 0
    target = "XMAS"

    directions = [
        (0,1), (1,1), (1,0), (1,-1),
        (0,-1), (-1,1), (-1,0), (-1,-1)
    ]

    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                # Check if word fits in this direction
                if (0 <= row + 3*dx < rows and 
                    0 <= col + 3*dy < cols):  # 3 because XMAS is 4 chars, need room for 3 more
                    # Build word in this direction
                    word = ''
                    for i in range(4):  # XMAS is 4 characters
                        word += maze_lines[row + i*dx][col + i*dy]
                    if word == target:
                        xmas_found += 1
    
    return xmas_found

def main():
    input_lines()
    print(search_maze())

main()
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

    similarity_sum = 0

    for i in range(len(list_left)):
        similarity_count = 0
        current_left_item = list_left[i]

        for j in range(len(list_right)):
            if list_right[j] == current_left_item:
                similarity_count += 1
            
        similarity = current_left_item * similarity_count
        similarity_sum += similarity
    
    print(similarity_sum)

main()

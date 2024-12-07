# This solution comes from https://www.reddit.com/r/adventofcode/comments/1h5frsp/comment/m0sng3n/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# This was an opportunity for us to see what a more compact solution looks like

import re 

with open("input.txt", "r") as file:
    corrupted_memory = file.read()

    corrupted_memory = re.sub(r"don't\(\).*?(?=do\(\)|$)", "", corrupted_memory, flags=re.DOTALL)
    occurences = re.findall("mul\(\d+,\d+\)", corrupted_memory)
    digits = [re.findall("\d+", occurence) for occurence in occurences]
    
    print(sum([int(pair[0]) * int(pair[1]) for pair in digits]))
from typing import List

def read_integers() -> List[int]:
    user_input = (input().split(","))
    numbers = []
    for number in user_input:
        numbers.append(int(number))
    return numbers

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

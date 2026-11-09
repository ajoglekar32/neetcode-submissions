def add_two_numbers() -> int:
    sum = 0
    user_input = input().split(",")
    for num in user_input:
        sum += int(num)
    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

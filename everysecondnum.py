def sum_numbers(a: int, b: int) -> int:
    return a + b


def divide_numbers(a: int, b: int) -> float:
    return a / b


def sub_numbers(a: int, b: int) -> int:
    return a - b


def mult_numbers(a:int, b: int) -> int:
    return a * b


first_input = input("number")
action_input = input("action")
last_input = input("number")
print(input, action_input, last_input)

if action_input == '+':
    result = sum_numbers(int(first_input),int(last_input))
elif action_input == '/':
    result = divide_numbers(int(first_input), int(last_input))
elif action_input == '-':
    result = sub_numbers(int(first_input), int(last_input))
elif action_input == '*':
    result =mult_numbers(int(first_input), int(last_input))

print(result)


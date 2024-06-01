import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)

    return expression, answer

wrong = 0
input("Press enter to start!")
print("--------------------------")

start = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = problem()
    while True:
        guess = input(f"Problem # {i+1}: {expression}: ")
        if guess == str(answer):
            break
        wrong += 1

end = time.time()
total = round(end - start, 2)

print("--------------------------")
print(f"Well done! You finished in {total} seconds.")
print(f"You made {wrong} wrong guesses")
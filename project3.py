import random
import time

OPERATORS = ["+", "-", "*", "/", "%"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 7


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = round(eval(expr), 1)
    return expr, answer


wrong = 0
print("\nMath Quiz!")
print("   Enter the answers as quickly as you can with as few mistakes as possible.")
print("   This quiz uses the operators", OPERATORS)
print("   For division round to 1 decimal place")
input("\nPress enter to Start!")
print("------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("------------------------")
print("Nice work! You finished in", total_time, "seconds! And you got", wrong, "incorrect.")

import random
import time


wrong = 0
input("Press Enter to start!")
print("----------------")


Operators = ["+", "-", "/", "*"]
Min_Operand = int(input("Minimum number for operations? "))
Max_Operand = int(input("Maximum number for operation? "))
Total_Problem = int(input("How many questions would you like to answer? "))


def generate_problem():
    left = random.randint(Min_Operand, Max_Operand)
    right = random.randint(Min_Operand, Max_Operand)
    operator = random.choice(Operators)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, round(answer, 1)


def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    if hours > 0:
        return f"{hours} hours, {minutes} minutes, {seconds} seconds"
    elif minutes > 0:
        return f"{minutes} minutes, {seconds} seconds"
    else:
        return f"{seconds} seconds"


start_time = time.time()
for i in range(Total_Problem):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem #{i + 1}: {expr} = ")
        try:
            guess = float(guess)
            if guess == answer:
                break
            else:
                wrong += 1
        except ValueError:
            print("Please enter a valid number.")



end_time = time.time()
total_time = end_time - start_time
formatted_time = format_time(total_time)


print("----------------")
print(f"Nice work! You finished in {formatted_time}.")
print(f"You got {wrong} wrong answers.")

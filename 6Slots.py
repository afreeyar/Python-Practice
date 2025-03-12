import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1 
ROWS = 3
COLS = 3


symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slots_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slots_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Invalid input. Please enter a number.")


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Invalid input. Please enter a number.")


def get_bet():
    while True:
        amount = input(f"Enter the amount you would like to bet on each line: ${MIN_BET} - ${MAX_BET}: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a number.")


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount. Your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}.")
    slots = get_slots_machine_spin(ROWS, COLS, symbol_count)
    print_slots_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")
    else:
        print("No winning lines.")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press enter to spin or 'q' to quit: ").strip().lower()
        if answer == 'q':
            print(f"Thanks for playing! You leave with ${balance}.")
            break
        elif balance <= 0:
            print("You don't have enough balance to continue playing.")
            break
        else:
            balance += spin(balance)


main()

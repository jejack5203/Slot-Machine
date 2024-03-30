import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8,
}  # how many times a symbol can appear in a single spin

symbol_values = {
    "A": 6,
    "B": 4,
    "C": 3,
    "D": 2,
}  # what the sybmols are worth (points) ex: D more commonly appears so it is worth less


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):  # loops through every row
        symbol = columns[0][
            line
        ]  # whatever symbol in the first column in row everything needs to match
        for column in columns:
            symbol_to_check = column[
                line
            ]  # symbol to check has to be equal to the coloumn at the row we are looking at
            if symbol != symbol_to_check:  # if they are not the same break no wins
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for (
        symbol,
        symbol_count,
    ) in symbols.items():  # looping through each individual symbol
        for _ in range(symbol_count):
            all_symbols.append(symbol)  # adding to all_symbol list

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


def print_slot_machine(columns):
    # transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():  # checks if input is a digit
            amount = int(amount)
            if amount > 0:  # checks if deposit amount is greater than 0
                break
            else:
                print(
                    "Amount must be greater than 0."
                )  # if not prompt user to input number greater than 0
        else:
            print("Please enter a number.")  # if amount does not pass isdigit

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-"
            + str(MAX_LINES)
            + ")? "  # str converts MAX_LINES to a string datatype
        )
        if lines.isdigit():  # checks if input is a digit
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a vaild number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():  # checks if input is a digit
            amount = int(amount)
            if (
                MIN_BET <= amount <= MAX_BET
            ):  # checks if user input is between the bounds of what can be betted
                break
            else:
                print(f"Amount must be between ${MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if (
            total_bet > balance
        ):  # checks to make sure you are not betting more than your balance
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}"
            )
        else:
            break

    print(
        f"Your are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You Won {winnings}.")
    print(f"You Won on lines: " "and" * winnings_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        if balance == 0:
            break

    print(f"You left with ${balance}")


main()

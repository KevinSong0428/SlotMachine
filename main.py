import random

# constant value is all caps
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolValues = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    # user is betting for 1 line, 2 lines, or all 3 lines - top to bottom
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            check = col[line]
            if check != symbol:
                # will check the next ROW if symbols are not the same
                break
        # for else loop <-- if it breaks, else is not executed
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)

    return winnings, winningLines


def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            allSymbols.append(symbol)

    # the randomly generated symbols are chosen from a VERTICAL list!
    # that's why we make a random column
    columns = []
    for _ in range(cols):
        column = []
        # slicing allSymbols makes a COPY at a new address
        # will not affect the original list of symbols
        currSymbols = allSymbols[:]
        for _ in range(rows):
            # randomly choose symbol then remove from the list
            value = random.choice(currSymbols)
            currSymbols.remove(value)
            # however many rows amount of symbols in every column
            column.append(value)

        columns.append(column)

    return columns


def printSlotMachine(columns):
    # need to transpose this matrix since we have it vertical
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                # end tells the statement what to actually end with
                print(col[row], end=" | ")
            else:
                print(col[row], end="\n")


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # checks to see if the amount entered is 0 or greater and if input is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                # break out of while loop if input is a valid integer greater than 0
                break
            else:
                print("Amount must be greater than $0.")
        else:
            print("Please enter a number.")
    return amount


def getNumberOfLines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                # break out of while loop if input is a valid integer and within the range
                break
            else:
                print("Amount must be between 1 and " + str(MAX_LINES) + ".")
        else:
            print("Please enter a valid number of lines.")
    return lines


def getBet(balance, lines):
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET and (bet * lines) <= balance:
                # break out of while loop if input is a valid integer and within the range
                break
            else:
                print(
                    f"INSUFFICIENT BALANCE! Amount must be between ${MIN_BET} - ${MAX_BET}. You tried placing a total bet of ${bet * lines}. Your balance is ${balance}.")
        else:
            print("Please enter a valid amount to bet.")
    return bet


def game(balance):
    lines = getNumberOfLines()
    bet = getBet(balance, lines)
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is ${lines * bet}.")
    slots = getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)
    earning, winningLines = checkWinnings(slots, lines, bet, symbolValues)
    balance = balance - (bet * lines) + earning
    if earning:
        print(f"You won ${earning}!")
        # this is the unpack operator on list
        print(f"You won on lines:", *winningLines)
    else:
        print(f"You lost!")
    print(f"Your current balance is ${balance}.")
    return balance


def main():
    balance = deposit()
    while True:
        spin = input("Press enter to spin. (Press q to quit). ")
        if spin == 'q':
            break
        balance = game(balance)
    print(f"You left with ${balance}.")


main()

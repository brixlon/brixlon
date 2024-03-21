import random #random ass values


MAX_LINES = 3 #basically my global constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS =3
symbol_count ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns,lines,bet,value):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]#makes a copy of the list so you can change stuff
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        column.append(column)
    return columns

def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i,column in enumerate (columns):
            if i != len(columns) -1: #checks max index
               print(column[row],end="|")
            else:
                print(column[row],end="")

        print()





def deposit():
    while True:
        amount =input("how much are you depositing ")
        if amount.isdigit():
            amount = int(amount) #typecasting input to avoid error
            if amount > 0:
                break
            else:
                print('amount must be greater than 0')
        else:
            print('enter a number')

    return amount


def no_of_lines ():
     while True:
        lines = input("enter number of lines to bet on(1-"+ str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines) #typecasting input to avoid error
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('enter valid no of lines')
        else:
            print('enter a number')
    
     return lines

def get_bet():
    while True:
        amount =input("how much are you betting on each line ")
        if amount.isdigit():
            amount = int(amount) #typecasting input to avoid error
            if MIN_BET<=amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET}  and {MAX_BET}")
        else:
            print('enter a number')

    return amount


def spin (balance):
    lines = no_of_lines()
    while True:  
     bet = get_bet()
     total_bet = bet*lines

     if total_bet > balance:
         print(f"insufficient funds,current balance {balance}")
     else:
         break
    print(f"you are betting {bet} on {lines}"
       f"total bet is ${total_bet}")
 
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)#spin mechanism
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,symbol_value)
    print(f'you won ${winnings}'
       f'you won on',*winning_lines)
    return winnings-total_bet



def main():
 balance = deposit()
 while True:
     print(f'current balance is $ {balance}')
     answer = input("press enter spin (q to quit)")
     if answer.lower() == "q":
         break
     balance += spin()

print("you left with ${balanced_tree}")
 

main()
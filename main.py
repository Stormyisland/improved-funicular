MAX_LINES = 3
MAX_BET = 21000000
MIN_BET = 1

def deposit():
    while True:
        amount = input("How much you got to give? $")
        if amount.isdigit():
            amount = int(amount)
            if amount  > 0:
                break
            else:
                print ("Come on who you kidding cough it up. Bub!")
        else:
            print("Give me some money.") 
            
    return amount    


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + " )? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print ("Come on give me Number of lines to bet on man.")
        else:
            print("bet some lines.") 
            
        return lines

def get_bet():
    while True:
        amount = input("How much you got to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Come on who you kidding cough it up. you need to enter an amount between ${MIN_BET} - ${MAX_BET} Bub!")
        else:
            print("Give me some money.") 
            
        return amount   
            
def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet() 
    total_bet  = bet * lines
    while True:
        if total_bet > balance:
            print(f"You dont have enough cash my man, your too broke, your current balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")


    
main()               
MAX_LINES =3

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
            print("Give me sone money.") 
            
    return amount    

def get_number_of_lines():
      while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + " )? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <=lines <= MAX_LINES:
                break
            else:
                print ("Come on give me Number of lines to bet on man.")
        else:
            print("bet some lines.") 
            
        return lines             
def main():
   balance = deposit()
   lines = get_number_of_lines() 
   print(balance, lines)
    
main()               
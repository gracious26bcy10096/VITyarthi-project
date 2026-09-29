from app.data import names, values
from app.calculator import convert
from app.display import table

def run_app():
    while True:
        print("\n----Currency converter----")
        print("\n1. Entry")
        print("2. Exit")
        opt = input("\nEnter 1 or 2:")
        
        if opt == "1":
            table(0)
            c1 = input("\nCurrency you have (e.g., USD, INR):")
            c2 = input("Currency you want (e.g., EUR, JPY):")
            amt = int(input("Amount to convert:"))
            c1 = c1.upper()
            c2 = c2.upper()

            if c1 in names and c2 in names:
                idx1 = names.index(c1)
                idx2 = names.index(c2)
                value1 = values[idx1]
                value2 = values[idx2]
                ans = convert(amt, value1, value2)
                print("\nResult:", ans, c2)

            elif c1 not in names:
                print("\nError: We don't have that first currency in our list.")
            elif c2 not in names:
                print("\nError: We don't have that second currency in our list.")

        elif opt == "2":
            print("\nGoodbye!,Thank you for using the currency converter.")
            break
        
        else:
            print("\nInvalid input, Please enter 1 or 2.")

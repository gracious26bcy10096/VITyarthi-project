names = ["USD", "EUR", "GBP", "INR", "JPY", 
    "CAD", "AUD", "AED", "CHF", "CNY", 
    "SEK", "NZD", "SGD", "HKD", "NOK", 
    "KRW", "TRY", "RUB", "BRL", "ZAR",
    "MXN", "SAR", "THB", "IDR", "MYR",
    "PHP", "DKK", "PLN", "CZK", "HUF"
]

values = [1.00, 0.88, 0.75, 95.82, 157.25, 
    1.41, 1.50, 3.67, 0.90, 7.15, 
    10.50, 1.60, 1.28, 7.80, 10.70, 
    1350.00, 34.20, 92.50, 5.50, 17.50,
    17.76, 3.75, 32.40, 15150.00, 4.13,
    56.10, 6.56, 3.85, 22.35, 348.50
]

def convert(amt, value1, value2):
    amt = float(amt)
    step1 = amt / value1
    step2 = step1 * value2
    return round(step2, 2)
def table(x):
    print("\n Available Currencies:")
    print("-"*22)
    print(names[0:10])
    print(names[10:20])
    print(names[20:30])

#frontend
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
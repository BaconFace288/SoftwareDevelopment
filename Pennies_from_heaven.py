dollar_100 = 10000
dollar_50 = 5000
dollar_20 = 2000
dollar_10 = 1000
dollar_5 = 500
dollar_1 = 100
half_dollar = 50
quarter = 25
dime = 10
nickel = 5
penny = 1

def change_conversion():
    penny_amount = int(input("Enter the amount of pennies you wish to convert: "))
    penny_amount >= 10000
    print("100 dollar bills = ", penny_amount // 10000)
    if penny_amount % 10000 != 0:
        penny_amount = penny_amount % 10000
    else:
        end_program = True
    penny_amount >= 5000
    print("50 dollar bills = ", penny_amount // 5000)
    if penny_amount % 5000 != 0:
        penny_amount = penny_amount % 5000
    else:
        end_program = True
    penny_amount >= 2000
    print("20 dollar bills = ", penny_amount // 2000)
    if penny_amount % 2000 != 0:
        penny_amount = penny_amount % 2000
    else:
        end_program = True
    penny_amount >= 1000
    print("10 dollar bills = ", penny_amount // 1000)
    if penny_amount % 1000 != 0:
        penny_amount = penny_amount % 1000
    else:
        end_program = True
    penny_amount >= 500
    print("5 dollar bills = ", penny_amount // 500)
    if penny_amount % 500 != 0:
        penny_amount = penny_amount % 500
    else:
        end_program = True
    penny_amount >= 200
    print("2 dollar bills = ", penny_amount // 200)
    if penny_amount % 200 != 0:
        penny_amount = penny_amount % 200
    else:
        end_program = True
    penny_amount >= 100
    print("1 dollar bills = ", penny_amount // 100)
    if penny_amount % 100 != 0:
        penny_amount = penny_amount % 100
    else:
        end_program = True
    penny_amount >= 50
    print("Half dollars = ", penny_amount // 50)
    if penny_amount % 50 != 0:
        penny_amount = penny_amount % 50
    else:
        end_program = True
    penny_amount >= 25
    print("Quarters = ", penny_amount // 25)
    if penny_amount % 25 != 0:
        penny_amount = penny_amount % 25
    else:
        end_program = True
    penny_amount >= 10
    print("Dimes = ", penny_amount // 10)
    if penny_amount % 10 != 0:
        penny_amount = penny_amount % 10
    else:
        end_program = True
    penny_amount >= 5
    print("Nickels = ", penny_amount // 5)
    if penny_amount % 5 != 0:
        penny_amount = penny_amount % 5
    else:
        end_program = True
    penny_amount >= 1
    print("Pennies = ", penny_amount // 1)
    end_program = True
    if penny_amount == 0:
        end_program = True



change_conversion()
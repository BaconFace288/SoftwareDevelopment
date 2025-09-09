print("Welcome, what is your name?")
customer_name = input()

starting_balance = 5000.25

print("Hello " + customer_name + " your starting balance is $" + str(starting_balance) + ".")

print("How much of your paycheck would you like to deposit?")
pay_check = float(input())

print("Looks like you went shopping? What did you buy?")
expenditure_item = input()

print("How much does " + expenditure_item + " cost?")
expenditure = float(input())

def checking_balance():
    balance = starting_balance
    deposits = pay_check
    expense_amount = expenditure
    ending_balance = balance + deposits - expense_amount
    print(f"Good day {customer_name}. After spending money on {expenditure_item} in the amount of ${expenditure}, your current checking balance is: ${ending_balance}")

checking_balance()
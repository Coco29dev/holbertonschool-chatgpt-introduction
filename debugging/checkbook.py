class Checkbook:
    def __init__(self):
        # Initializes the balance to 0.0
        self.balance = 0.0

    def deposit(self, amount):
        # Adds the deposit amount to the current balance
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Checks if the withdrawal amount is greater than the current balance
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            # Deducts the withdrawal amount from the balance
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Displays the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    while True:
        try:
            # Ask the user for an amount and attempt to convert it to a float
            amount = float(input(prompt))
            if amount < 0:
                # Reject negative amounts
                print("Amount must be a positive number. Please try again.")
            else:
                return amount
        except ValueError:
            # Catch ValueError if the user enters a non-numeric value
            print("Invalid input! Please enter a valid number.")

def main():
    cb = Checkbook()
    
    while True:
        # Ask the user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            # Exit the loop and end the program
            break
        elif action == 'deposit':
            # Prompt for the deposit amount and validate it
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            # Prompt for the withdrawal amount and validate it
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            # Show the current balance
            cb.get_balance()
        else:
            # Handle invalid commands
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

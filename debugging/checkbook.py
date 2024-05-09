class Checkbook:
    def __init__(self):
        """
        Initializes a new Checkbook object with a balance of $0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
        - amount (float): The amount to be deposited.

        Returns:
        None
        """
        try:
            amount = float(amount)  # Convert input to float
            if amount <= 0:
                print("Invalid amount. Amount must be a positive number.")
                return
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook, if sufficient funds are available.

        Parameters:
        - amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        try:
            amount = float(amount)  # Convert input to float
            if amount <= 0:
                print("Invalid amount. Amount must be a positive number.")
                return
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    def get_balance(self):
        """
        Retrieves the current balance of the checkbook.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

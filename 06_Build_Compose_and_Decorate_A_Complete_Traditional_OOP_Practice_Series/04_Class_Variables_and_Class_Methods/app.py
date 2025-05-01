class Bank:
    bank_name = "ABC Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Changing class variable using cls


# Example usage
acc1 = Bank("Ayesha")
acc2 = Bank("Ali")

# Accessing class variable from instances
print("Before change:")
print("Account 1 Bank:", acc1.bank_name)
print("Account 2 Bank:", acc2.bank_name)

# Changing bank name using class method
Bank.change_bank_name("XYZ Bank")

print("\nAfter change:")
print("Account 1 Bank:", acc1.bank_name)
print("Account 2 Bank:", acc2.bank_name)

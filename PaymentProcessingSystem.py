

class DebitCard:
    def pay(self, amount):
        print(f"₹{amount} was paid using the Debit Card payment method.")


class UPI:
    def pay(self, amount):
        print(f"₹{amount} was paid using the UPI payment method.")


class CreditCard:
    def pay(self, amount):
        print(f"₹{amount} was paid using the Credit Card payment method.")




class Payment:
    def __init__(self, method):
        self.method = method

    def set_method(self, method):
        self.method = method

    def make_payment(self, amount):
        self.method.pay(amount)



print("Payment Methods")
print("1. Debit Card")
print("2. UPI")
print("3. Credit Card")

choice = int(input("Enter your choice: "))
amount = float(input("Enter the amount to be paid: "))

p = Payment(DebitCard())

if choice == 1:
    p.set_method(DebitCard())
elif choice == 2:
    p.set_method(UPI())
elif choice == 3:
    p.set_method(CreditCard())
else:
    print("Invalid choice")
    exit()

p.make_payment(amount)
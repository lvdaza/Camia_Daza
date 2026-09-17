#Hi sir, maawa ka sakin plz thxxx

valid_payment = {"Cash", "GCash", "Card"}

payment = input("Enter your payment: ").lower()

if payment in valid_payment:
    print("Payment Successful:", payment.capitalize())
else:
    print("Invalid payment method:", payment.capitalize())


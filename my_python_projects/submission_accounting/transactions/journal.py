print('[Module] Journal loaded.')


def receive_income(amount):
    print("[Journal] Received R{}.00".format(amount))
    
def pay_expense(amount):
    print("[Journal] Paid R{}.00".format(amount))
    
def Journal():
    amount = "100"
    receive_income(amount)
    pay_expense(amount)

if __name__ == "__main__":
    Journal()
    
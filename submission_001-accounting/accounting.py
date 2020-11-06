import sys


from user.authentication import authenticate_user
from transactions.journal import receive_income
from transactions.journal import pay_expense
import banking


if len(sys.argv) > 1:
    commandline_arguments = list(filter(lambda argument: argument != sys.argv[0], sys.argv))
    print("\n".join(commandline_arguments))


if __name__ == "__main__":
    # help("modules")
    authenticate_user()

    amount = 100
    receive_income(amount)
    pay_expense(amount)
    
    banking.do_reconciliation()
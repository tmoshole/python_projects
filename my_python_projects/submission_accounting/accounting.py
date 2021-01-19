import sys
import requests
import user.authentication
import transactions.journal
import banking
#import banking.fvb.reconciliation
#import banking.ubsa.reconciliation
#import banking.online.reconciliation

if __name__ == "__main__":
    #help("modules")
    if len(sys.argv) > 1:
        k = 1
        for x in range(len(sys.argv)-1):
            print(sys.argv[k])
            k += 1
    user.authentication.authenticate_user()
    transactions.journal.Journal()
    #banking.reconciliation.do_reconciliation()
    banking.fvb.reconciliation.do_reconciliation()
    #banking.ubsa.reconciliation.do_reconciliation()
    #banking.online.reconciliation.do_reconciliation()
     
import requests
print('[Module] online.Reconciliation loaded.')

def do_reconciliation():
    print('Doing Online Bank reconciliation.')

    response = requests.get('https://www.wethinkcode.co.za')
    print(response.status_code)
    

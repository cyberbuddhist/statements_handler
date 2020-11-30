import requests
# import json
import urllib3
import OrdersVars


urllib3.disable_warnings()


def openfile():
    host = 'https://risk-pp.alfaleasing.ru/statements/statements_handler/'
    data = {
        'inn': '7703449272',
        'min_period_months': 12,
        'bad_transaction_rate_limit': 0.06
    }
    with open('альфа.txt', 'rb') as file:
        files = {'files': file}
        '''
        json_data = json.dumps(data)
        headers = {'Content-type': 'application/json'}
        '''
        response = requests.post(host, files=files, data=data, headers="", verify=False)
        return response.text


'''
вопрос по сервису statements handler?
если я отправляю в него запрос не из django и не из jupyter, а из PyCharm, как мне прописать кодом токен авторизации?
if __name__ == '__main__':
    das = OrdersVars()
    print(das)
    das.clientBankDocFull()
    #print(BankPlat)
    #print("currentDataString: " + order.currentDataString)
    #print("currentTimeString: " + order.currentTimeString)
    #print("Random data: " + order.randomDate)
    #print("Random time: " + order.randomTime)
    #for x in range(10): print("Random numbers: " + order.gen_random_number(9))
'''
if __name__ == '__main__':
    doc = OrdersVars.make()
    print(doc)

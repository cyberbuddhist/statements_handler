import requests
import json
import urllib3
import OrdersVars
from OrdersVars import make
urllib3.disable_warnings()


    doc = OrdersVars.make()
#def serverRequest():
    host = 'https://risk-pp.alfaleasing.ru/statements/statements_handler/'
    data = {
        'inn': '7703449272',
        'min_period_months': 12,
        'bad_transaction_rate_limit': 0.06
    }
    with open(doc, 'rb') as file:
        files = {'files': file}
        json_data = json.dumps(data)
        headers = {'Content-type': 'application/json'}
        response = requests.post(host, files = files, data = data, headers = headers, verify=False)
    response.text
    #result = response
    #print(result)
    #return result.text
    #server_answer = serverRequest()


#if __name__ == '__main__':
    '''
    doc = OrdersVars.make()
    json_data = json.dumps(doc)
    headers = {'Content-type': 'application/json'}
    response = requests.post(host, files=files, doc=data, headers="", verify=False)
    result = response
    print(result)
    '''
    #server_answer = ServerRequest()



'''вопрос по сервису statements handler?
если я отправляю в него запрос не из django и не из jupyter, а из PyCharm, как мне прописать кодом токен авторизации?'''
#if __name__ == '__main__':
   # das = OrdersVars()
   # print(das)
    #das.clientBankDocFull()
    #print(BankPlat)
    #print("currentDataString: " + order.currentDataString)
    #print("currentTimeString: " + order.currentTimeString)
    #print("Random data: " + order.randomDate)
    #print("Random time: " + order.randomTime)
    #for x in range(10): print("Random numbers: " + order.gen_random_number(9))

'''if __name__ == '__main__':
    doc = OrdersVars.make()
    print(doc)
    return doc.text'''

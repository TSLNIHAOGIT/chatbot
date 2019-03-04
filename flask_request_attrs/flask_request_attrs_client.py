import requests
import json
def post_test():
    for i in range(4):
        res = requests.post('http://localhost:5000/api/add_message{}/1234'.format(i),
                            json={
                                "mytext0":"from client :lalala",
                                "mytext1":"from client :lalala",
                                "mytext2":"from client :lalala",
                                "mytext3":"from client :lalala",
                                "mytext4":"from client :lalala",
                                "mytext5": "from client :lalala",
                                "mytext6": "from client :lalala",
                                "mytext7": "from client :lalala",
                                "mytext8": "from client :lalala",
                                "mytext9": "from client :lalala",
                            })

        if res.ok:
            print('res.json()',res.json())

        '''
        >>> url = 'https://api.github.com/some/endpoint'
        >>> payload = {'some': 'data'}
        
        >>> r = requests.post(url, data=json.dumps(payload))#data后面需要序列化
        或者
        >>> r = requests.post(url, json=payload)#json直接传递字典
        '''

        res = requests.post('http://localhost:5000/api/add_message{}/1234'.format(i),

                            #data为关键字传递时需要进行序列化之后传递，否则为乱码；json为关键字时则直接传递dict即可
                            data=json.dumps({
                                "mytext0": "from client :lalala",
                                "mytext1": "from client :lalala",
                                "mytext2": "from client :lalala",
                                "mytext3": "from client :lalala",
                                "mytext4": "from client :lalala",
                                "mytext5": "from client :lalala",
                                "mytext6": "from client :lalala",
                                "mytext7": "from client :lalala",
                                "mytext8": "from client :lalala",
                                "mytext9": "from client :lalala",
                            }))
        if res.ok:
            print('res.json()',res.json())




def get_test():

    payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
    r = requests.get('http://localhost:5000/api/add_message_get/1234', params=payload)
    print('content',r.content.decode('utf8'))
    pass
if __name__=='__main__':
    post_test()
    # get_test()
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/api/add_message_get/<uuid>', methods=['GET', 'POST'])
def add_message_get(uuid):
    #可以获取未经处理过的原始数据，如果数据格式是json的，则取得的是json字符串，排序和请求参数一致
    content = request.data
    print('request.data content',content)
    return 'server 返回的数据'


@app.route('/api/add_message0/<uuid>', methods=['GET', 'POST'])
def add_message0(uuid):
    #可以获取未经处理过的原始数据，如果数据格式是json的，则取得的是json字符串，排序和请求参数一致
    content = request.data
    print('request.data content',content)
    return jsonify({"uuid":uuid})

@app.route('/api/add_message1/<uuid>', methods=['GET', 'POST'])
def add_message1(uuid):
    #获取未经处理过的原始数据而不管内容类型,如果数据格式是json的，则取得的是json字符串，排序和请求参数一致
    content = request.get_data()
    print('request.get_data() content',content.decode('gbk'))
    return jsonify({"uuid":uuid})




@app.route('/api/add_message2/<uuid>', methods=['GET', 'POST'])
def add_message2(uuid):
    #.将请求参数做了处理，得到的是字典格式的，因此排序会打乱依据字典排序规则
    content = request.json
    print('request.json content',content)
    return jsonify({"uuid":uuid})


#服务端获取客户端发来的json数据
@app.route('/api/add_message3/<uuid>', methods=['GET', 'POST'])
def add_message3(uuid):
    #将请求参数做了处理，得到的是字典格式的，因此排序会打乱依据字典排序规则
    content = request.get_json(silent=True,force=True)
    print('request.get_json() content',content) # Do your processing
    #response must be a string\tupe\ and so on.
    return jsonify(content)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    response = 'Hello, world!'
    error_message = 'This method is unsupported.'
    if request.method == 'GET':
        return response, 200
    else:
        return error_message, 405 

@app.route('/test', methods=['GET', 'POST'])
def test():
    get_response = 'Get message received'
    post_response = 'Post message received: '
    error_message = 'This method is unsupported.'
    if request.method == 'GET':
        return get_response, 200
    else:
        request_msg = request.args.get('msg')
        if request_msg:
            return post_response + request_msg, 200
        else:
            return error_message, 405 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8081)



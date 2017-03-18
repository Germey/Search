from flask import Flask, request
from flask import jsonify

from baidu import get_request as request_baidu
from bing import get_request as request_bing

app = Flask(__name__)

@app.route('/baidu', methods=['POST'])
def baidu():
    keyword = request.form['keyword']
    total = request.form['total']
    total = int(total)
    return jsonify(request_baidu(keyword, total))

@app.route('/bing', methods=['POST'])
def bing():
    keyword = request.form['keyword']
    total = request.form['total']
    total = int(total)
    return jsonify(request_bing(keyword, total))

if __name__ == '__main__':
    app.run()

from flask import Flask, request
from flask import jsonify

from baidu import get_request

app = Flask(__name__)

@app.route('/baidu', methods=['POST'])
def baidu():
    keyword = request.form['keyword']
    total = request.form['total']
    total = int(total)
    return jsonify(get_request(keyword, total))

if __name__ == '__main__':
    app.run()

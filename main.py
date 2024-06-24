from flask import Flask, jsonify, abort
import time
import random
import string

app = Flask(__name__)

@app.route('/<int:accountId>/data')
def get_data(accountId):
    timestamp = time.time()
    data = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return jsonify({
        "accountId": accountId,
        "timestamp": timestamp,
        "data": data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

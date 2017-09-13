from flask import Flask, jsonify
from statistic import Statistic

app = Flask(__name__)

@app.route('/')
def get():
    stat = Statistic()
    result = stat.get()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

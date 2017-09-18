from flask import Flask, jsonify
from statistic import Statistic

app = Flask(__name__)

@app.route('/')
def get_all():
    stat = Statistic()
    result = stat.get()
    return jsonify(result)

@app.route('/get/<id>')
def get_detail(id):
    stat = Statistic()
    result = stat.get_detail(id)
    return jsonify(result)

@app.route('/get/unames')
def get_unames():
    stat = Statistic()
    result = stat.get_unames()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

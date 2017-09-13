from flask import Flask, jsonify
from statistic import Statistic

app = Flask(__name__)

@app.route('/')
def get():
    stat = Statistic()
    result = stat.get()
    return jsonify(result)


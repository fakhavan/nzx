from flask import Flask, jsonify, render_template, request
from nzx_stocks import nzx_stocks
from waitress import serve
import json

nzx_data_rest = Flask(__name__)

@nzx_data_rest.route('/api/v1/latest/list_all', methods=["GET"])
def return_latest_mainboard_pull():
    return nzx_stocks().as_dict(), 200


if __name__ == "__main__":
    #nzx_data_rest.run(debug=1)
    serve(nzx_data_rest, host="0.0.0.0", port=5000)
    
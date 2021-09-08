from flask import Flask, request
from flask_ngrok import run_with_ngrok
from stockapis.stock_encoder import StockEncoder
from stockapis.stock_data_handler import StockDataHandler

web_app = Flask(__name__)

run_with_ngrok(web_app)


@web_app.route("/connect", methods=['GET'])
def connect():
    return "this is a test"


@web_app.route("/getstockdetails/<code>", methods=['GET', 'POST'])
def post_calling(code):
    if request.method == 'GET':
        stock_data_handler_object = StockDataHandler(code)
        stock_encoder_object = StockEncoder()
        stock_data = stock_data_handler_object.get_stock_data()
        json_stock_data = stock_encoder_object.encode(stock_data)
        return json_stock_data


if __name__ == "__main__":
    web_app.run()

from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from stockapis.stock_encoder import StockEncoder
from stockapis.stock_data_handler import StockDataHandler
from stockapis.log_maker import info, error

web_app = Flask(__name__)

run_with_ngrok(web_app)


@web_app.route("/connect", methods=['GET'])
def connect():
    return "this is to check the website connection "


@web_app.route("/getstockdetails/<code>", methods=['GET', 'POST'])
def post_calling(code):
    try:
        if request.method == 'GET':
            info("Debug : api called for " + str(code))
            stock_data_handler_object = StockDataHandler(code)
            info("Debug : stock data handler created")

            info("Validating the stock code/company name ")
            if stock_data_handler_object.validate_stock_code():
                info("Debug : Valid stock code entered ")
                stock_encoder_object = StockEncoder()
                info("Debug : stock data handler created")
                stock_data = stock_data_handler_object.get_stock_data()
                json_stock_data = stock_encoder_object.encode(stock_data)
                info("Debug : Stock Data = " + json_stock_data)
                return json_stock_data
            else:
                info("Debug : invalid company code " + code)
                return jsonify(error_messgae="invalid Company Name please check once again ")
    except Exception as e:
        error("Error : error encounter " + str(e))
        return e

from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from stockapis.helper_classes.stock_encoder import StockEncoder
from stockapis.controller.stock_data_handler import StockDataHandler
from stockapis.helper_classes.helper import info, error

web_app = Flask(__name__)

run_with_ngrok(web_app)

stock_data_handler_object = StockDataHandler()

stock_encoder_object = StockEncoder()


# this is to check the connection of the application

@web_app.route("/connect", methods=['GET'])
def connect():
    return "this is to check the website connection "


# get Multiple Data in set of 10

@web_app.route("/multiple/<index>", methods=['GET', 'POST'])
def multiple(index):
    info("Debug : multiple stocks  data called with index{0}".format(str(index)))

    try:

        output_stocks = stock_data_handler_object.get_multiple_stock_data(int(index))

        if len(output_stocks) > 0:
            info("Debug : stock data received  ")

            json_stocks_data = stock_encoder_object.encode(output_stocks)
            info("Debug : returned stocks data =  {0}".format(str(json_stocks_data)))

            return json_stocks_data

        else:
            error("Error : no stock data received :")
            return None

    except Exception as e:
        error("Error : error encounter {0}".format(str(e)))
        return e


# To get one stock data

@web_app.route("/stock/<code>", methods=['GET', 'POST'])
def post_calling(code):
    try:
        if request.method == 'GET':
            info("Debug : api called for {0}".format(str(code)))

            info("Validating the stock code/company name ")

            if stock_data_handler_object.validate_stock_code(code):
                info("Debug : Valid stock code entered ")
                stock_data = stock_data_handler_object.get_stock_data(code)

                json_stock_data = stock_encoder_object.encode(stock_data)

                info("Debug : Stock Data = {0}".format(json_stock_data))

                return json_stock_data
            else:
                info("Debug : invalid company code {0}".format(str(code)))
                return jsonify(error_messgae="invalid Company Name please check once again ")
    except Exception as e:
        error("Error : error encounter {0}".format(str(e)))
        return e

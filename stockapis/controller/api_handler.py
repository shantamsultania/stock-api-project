from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok

from stockapis.agent_handler.stock_data_handler import StockDataHandler
from stockapis.helper_classes.helper import info, error
from stockapis.helper_classes.stock_encoder import StockEncoder

web_app = Flask(__name__, template_folder=r"D:\stock-api-project\stockapis\uiHandler\\templates")

run_with_ngrok(web_app)

stock_data_handler_object = StockDataHandler()

stock_encoder_object = StockEncoder()


# this is to check the connection of the application

@web_app.route("/connect", methods=['GET'])
def connect():
    return "this is to check the website connection "


# get Multiple Data in set of 10

@web_app.route("/multiple/<index>", methods=['GET'])
def multiple(index):
    info("Debug : multiple stocks  data called with index{0}".format(str(index)))

    try:

        output_stocks = stock_data_handler_object.get_multiple_stock_data(int(index))

        if len(output_stocks) > 0:
            info("Debug : stock data received  ")

            info("Debug : returned stocks data =  {0}".format(str(stock_encoder_object.encode(output_stocks))))
            return render_template("multiple_stock_viewer.html", stock_data=output_stocks)

        else:
            error("Error : no stock data received :")

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

            stock_data = []

            if stock_data_handler_object.validate_stock_code(code):
                info("Debug : Valid stock code entered ")
                stock_data.append(stock_data_handler_object.get_stock_data(code))

                info("Debug : Stock Data = {0}".format(stock_encoder_object.encode(stock_data)))

                return render_template("single_stock_view.html", stock_data=stock_data)
            else:
                info("Debug : invalid company code {0}".format(str(code)))
                return jsonify(error_messgae="invalid Company Name please check once again ")

    except Exception as e:
        error("Error : error encounter {0}".format(str(e)))
        return e

from nsetools import Nse

from stockapis.helper_classes.helper import info, stock_code_filter, lowercase_converter, stock_data_setter
from stockapis.model_classes.stock import Stock


class StockDataHandler:

    def __init__(self):
        self.nse = Nse()

    def validate_stock_code(self, stock_code):
        info("Debug : checking for valid company code")

        return self.nse.is_valid_code(stock_code)

    def get_all_stock_codes(self):
        info("Debug : stock codes are being fetched ")
        stock_codes = self.nse.get_stock_codes()
        stock_codes = lowercase_converter(stock_codes)
        return stock_codes

    def get_multiple_stock_data(self, index):
        info("Debug : get multiple data  ")

        codes = self.get_all_stock_codes()
        filtered_codes = stock_code_filter(codes, index)
        required_stock = []

        for code in filtered_codes:
            info("Debug : get multiple data  " + str(code))
            temp_stock = Stock()
            stock_data = self.nse.get_quote(code)

            info("Debug : Stock Data received from nse tool  = " + str(stock_data))

            temp_stock = stock_data_setter(temp_stock=temp_stock, stock_data=stock_data)

            required_stock.append(temp_stock)

        info("Debug : multiple stocks/required stocks = " + str(required_stock))
        return required_stock

    def get_stock_data(self, stock_code):
        info("Debug : getting stock data ")

        temp_stock = Stock()

        info("Debug : empty stock class initialized")

        stock_data = self.nse.get_quote(stock_code)

        info("Debug : Stock Data received from nse tool  = " + str(stock_data))

        temp_stock = stock_data_setter(temp_stock=temp_stock, stock_data=stock_data)

        info("Debug : stock data after formatting/filtering = " + str(temp_stock))
        return temp_stock

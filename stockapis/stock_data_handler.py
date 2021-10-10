from nsetools import Nse
from stockapis.stock import Stock
from stockapis.log_maker import info, error


class StockDataHandler:

    def __init__(self, stock_code):
        self.nse = Nse()
        self.stock_code = stock_code

    def validate_stock_code(self):

        info("Debug : checking for valid company code")

        return self.nse.is_valid_code(self.stock_code)

    def get_stock_data(self):

        info("Debug : getting stock data ")

        temp_stock = Stock()

        info("Debug : empty stock class initialized")

        try:
            stock_data = self.nse.get_quote(self.stock_code)

            info("Debug : Stock Data received from nse tool  = " + str(stock_data))

            temp_stock.set_day_low(stock_data['dayLow'])
            temp_stock.set_series(stock_data['series'])
            temp_stock.set_previous_close(stock_data['previousClose'])
            temp_stock.set_open_price(stock_data['open'])
            temp_stock.set_total_traded_volume(stock_data['totalTradedVolume'])
            temp_stock.set_low52(stock_data['low52'])
            temp_stock.set_is_in_code(stock_data['isinCode'])
            temp_stock.set_high52(stock_data['high52'])
            temp_stock.set_day_high(stock_data['dayHigh'])
            temp_stock.set_company_name(stock_data['companyName'])
            temp_stock.set_cm_adj_high_dt(stock_data['cm_adj_high_dt'])
            temp_stock.set_close_price(stock_data['closePrice'])
            temp_stock.set_buy_price(stock_data['buyPrice1'])
            temp_stock.set_base_price(stock_data['basePrice'])
            temp_stock.set_average_price(stock_data['averagePrice'])

        except Exception as e:

            error("error while getting the data " + str(e))

        info("Debug : stock = " + str(temp_stock))
        return temp_stock

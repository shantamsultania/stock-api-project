class Stock:

    def __init__(self, average_price=0, base_price=0,
                 buy_price=0, close_price=0, cm_adj_high_dt=0, company_name=None,
                 day_high=0, day_low=0, high52=0, series=None, total_traded_volume=0, is_in_code=None, low52=0,
                 open_price=0, previous_close=0):
        self._averagePrice = average_price
        self._basePrice = base_price
        self._buyPrice = buy_price
        self._closePrice = close_price
        self._cm_adj_high_dt = cm_adj_high_dt
        self._companyName = company_name
        self._dayHigh = day_high
        self._dayLow = day_low
        self._high52 = high52
        self._isinCode = is_in_code
        self._low52 = low52
        self._open_price = open_price
        self._previousClose = previous_close
        self._totalTradedVolume = total_traded_volume
        self._series = series

    def get_average_price(self):
        return self._averagePrice

    def get_base_price(self):
        return self._basePrice

    def get_buy_price(self):
        return self._buyPrice

    def get_close_price(self):
        return self._closePrice

    def get_cm_adj_high_dt(self):
        return self._cm_adj_high_dt

    def get_company_name(self):
        return self._companyName

    def get_day_high(self):
        return self._dayHigh

    def get_day_low(self):
        return self._dayLow

    def get_high52(self):
        return self._high52

    def get_low52(self):
        return self._low52

    def get_is_in_code(self):
        return self._isinCode

    def get_open_price(self):
        return self._open_price

    def get_previous_close(self):
        return self._previousClose

    def get_total_traded_volume(self):
        return self._totalTradedVolume

    def get_series(self):
        return self.series

    def set_average_price(self, avg_price):
        self._averagePrice = avg_price

    def set_base_price(self, base_price):
        self._basePrice = base_price

    def set_buy_price(self, buy_price):
        self._buyPrice = buy_price

    def set_close_price(self, close_price):
        self._closePrice = close_price

    def set_cm_adj_high_dt(self, cm_adj_high_dt):
        self._cm_adj_high_dt = cm_adj_high_dt

    def set_company_name(self, company_name):
        self._companyName = company_name

    def set_day_high(self, day_high):
        self._dayHigh = day_high

    def set_day_low(self, day_low):
        self._dayLow = day_low

    def set_high52(self, high_52_week):
        self._high52 = high_52_week

    def set_low52(self, low_52_week):
        self._low52 = low_52_week

    def set_is_in_code(self, isin_code):
        self._isinCode = isin_code

    def set_open_price(self, open_price):
        self._open_price = open_price

    def set_previous_close(self, previous_close):
        self._previousClose = previous_close

    def set_total_traded_volume(self, total_volume):
        self._totalTradedVolume = total_volume

    def set_series(self, series):
        self.series = series

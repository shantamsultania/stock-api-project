import logging
import schedule as schedule

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def debug(message):
    logging.debug(message)


def info(message):
    logging.error(message)


def error(message):
    logging.error(message)


def scheduler(function, time):
    def inner():
        schedule.every(time).seconds.do(function)
        return

    return inner


def stock_code_filter(codes, index):
    required_codes = []

    upper_limit = index * 25
    lower_limit = (index - 1) * 25
    print("{0} {1}".format(upper_limit, lower_limit))
    for i in range(0, len(codes)):
        if lower_limit < i <= upper_limit:
            required_codes.append(codes[i])
        if i > upper_limit:
            break

    return required_codes


def stock_data_setter(temp_stock, stock_data):
    try:

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

    return temp_stock


def lowercase_converter(input_dict):
    output = dict((key.upper(), value.upper()) for key, value in input_dict.items())
    output = list(output.keys())
    output.remove(output[0])
    return output

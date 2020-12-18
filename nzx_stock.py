import bs4
import requests

class nzx_instrument():
    def __init__(self):
        self.stock_ticker = None
        self.stock_name = None
        self.trading_status = None
        self.trades = None
        self.value = None
        self.volune = None
        self.capitalisation = None
        self.open = None
        self.high = None
        self.low = None
        self.high_bid = None
        self.low_offer = None
        self.pe = None
        self.eps = None
        self.nta = None
        self.gross_div = None
        self.num_securities = None


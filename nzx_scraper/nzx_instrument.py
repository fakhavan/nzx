from nzx_mainboard_stock import nzx_mainboard_stock
from bs4 import BeautifulSoup
import requests

class nzx_stocks():
    
    def __init__(self, url="https://www.nzx.com/markets/NZSX"):
        self.all_stocks_html = self.get_stock_list(url)
        self.stocks = []
        for stock_raw in self.all_stocks_html:
            self.stocks += [nzx_mainboard_stock(stock_raw)]

    def get_stock_list(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        all_stocks = soup.find(id="instruments-table").tbody.findAll('tr')
        return all_stocks
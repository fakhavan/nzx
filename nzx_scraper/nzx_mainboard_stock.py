from  bs4 import BeautifulSoup

class nzx_mainboard_stock():

    def __init__(self, stock_raw):
        self.ticker = self.get_stock_ticker(stock_raw)
        self.name = self.get_stock_name(stock_raw)
        self.price = self.get_stock_price(stock_raw)
        self.change = None
        self.value = None
        self.volume = None
        self.capitalisation = None

    def get_stock_ticker(self, stock_raw):
        result = None
        result = stock_raw.find('td').find('strong', class_="").text
        return result
    
    def get_stock_name(self, stock_raw):
        result = None
        result = stock_raw.find_all('a')[1].text
        return result

    def get_stock_price(self, stock_raw):
        result = None
        result = stock_raw.select('td[data-title="Price"]')[0].text.strip()[1:]
        return result
from  bs4 import BeautifulSoup

class nzx_mainboard_stock():

    def __init__(self, stock_raw):
        self.ticker = self.get_ticker(stock_raw)
        self.name = self.get_name(stock_raw)
        self.price = self.get_price(stock_raw)
        self.change = self.get_change(stock_raw)
        self.value = self.get_value(stock_raw)
        self.volume = self.get_volume(stock_raw)
        self.capitalisation = self.get_capitalisation(stock_raw)

    def get_ticker(self, stock_raw):
        result = None
        result = stock_raw.find('td').find('strong', class_="").text
        return result
    
    def get_name(self, stock_raw):
        result = None
        result = stock_raw.find_all('a')[1].text
        return result

    def get_price(self, stock_raw):
        result = None
        result = stock_raw.select('td[data-title="Price"]')[0].text.strip()[1:]
        return result
    
    def get_change(self, stock_raw):
        result = None
        result = stock_raw.select('td[data-title="ChangePercent"]')[0].text.strip()
        return result

    def get_value(self, stock_raw):
        result = None
        result = stock_raw.select('td[data-title="Value"]')[0].text.strip()[1:]
        return result

    def get_volume(self, stock_raw):
        result = None
        result = stock_raw.select('td[data-title="Volume"]')[0].text.strip()
        return result

    def get_capitalisation(self, stock_raw):
        result = None
        result = stock_raw.select('td[data-title="Capitalisation"]')[0].text.strip()
        return result
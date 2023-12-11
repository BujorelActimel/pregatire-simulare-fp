class Furniture:
    furniture_code = 0
    def __init__(self, type_: str, name: str, stock: int, price: float, code = None):
        if code:
            self._code = code
        else:
            self._code = Furniture.furniture_code
            Furniture.furniture_code += 1   
        self._type = type_
        self._name = name
        self._stock = stock
        self._price = price
    
    def __str__(self):
        return f"cod: {self.code}, nume: {self.name}, stock: {self.stock}, pret: {self.price}"

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def type_(self):
        return self._type

    @property
    def stock(self):
        return self._stock

    @property
    def price(self):
        return self._price

    @stock.setter
    def stock(self, value):
        self._stock = value

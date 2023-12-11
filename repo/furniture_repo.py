from furniture.furniture import Furniture

class FurnitureRepo:
    def __init__(self, file_name):
        self._file_name = file_name
        self._furniture_list = self.loadData()

    @property
    def file_name(self):
        return self._file_name

    @property
    def furniture_list(self):
        return self._furniture_list

    def loadData(self):
        furn_list = []

        with open(self.file_name, "r") as f:
            furniture_data = f.readlines()
        
        for furn in furniture_data[1:]:
            code, type_, name, stock, price = furn.strip().split(",")
            code = int(code)
            stock = int(stock)
            price = float(price)
            furn_list.append(Furniture(type_, name, stock, price, code=code))
        
        return furn_list

    def saveData(self):
        with open(self.file_name, "w") as f:
            f.write("code,type,name,stock,price\n")
            for furn in self.furniture_list:
                f.write(f"{furn.code},{furn.type_},{furn.name},{furn.stock},{furn.price}\n")

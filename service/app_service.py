class AppService:
    def __init__(self, repo):
        self._repo = repo
    
    @property
    def repo(self):
        return self._repo

    def searchByType(self, furniture_type):
        return [furn for furn in self.repo.furniture_list if furn.type_ == furniture_type and furn.stock > 0]

    def buy(self, furn_code, number_of_units):
        for furniture in self.repo.furniture_list:
            if furniture.code == furn_code:
                if furniture.stock >= number_of_units:
                    furniture.stock -= number_of_units
                    return round(number_of_units * furniture.price, 2)
                else:
                    raise ValueError("Prea putine unitati in stoc")
        
        raise ValueError(f"Nu a fost gasita piesa de mobilier cu cod {furn_code}")
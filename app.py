import os
from utils import Utility
from furniture import Furniture
from repo import FurnitureRepo
from service import AppService

class App:
    def __init__(self):
        self._utilities = Utility()
        self._repo = FurnitureRepo("data/furniture_data.csv")
        self._service = AppService(self.repo)

    @property
    def utilities(self):
        return self._utilities

    @property
    def repo(self):
        return self._repo
    
    @property
    def service(self):
        return self._service

    def menu(self):
        os.system("cls")
        print("""Choose a command:
        1 - Cauta Mobilier
        2 - Cumpara Mobilier
        3 - Exit"""
        )

    def run(self):
        while True:
            self.menu()
            command = self.utilities.get_command()

            if command == 1:
                type_input = self.utilities.get_text_input("Tipul de mobilier: ")
                results = self.service.searchByType(type_input)
                for result in results:
                    print(result)
                self.utilities.enter()

            if command == 2:
                furn_code = self.utilities.get_numerical_input("Cod mobilier: ")
                number_of_units = self.utilities.get_numerical_input("Numar bucati: ")
                try:
                    final_price = self.service.buy(furn_code, number_of_units)
                except ValueError as error:
                    self.utilities.enter(error)
                else:
                    self.utilities.enter(f"Tranzactie facuta cu succes, pretul este de {final_price}")

            if command == 3:
                self.repo.saveData()
                exit()


if __name__ == "__main__":
    app = App()
    app.run()

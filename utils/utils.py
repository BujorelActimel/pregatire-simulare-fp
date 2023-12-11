class Utility:

    def get_command(self):
        while True:
            try:
                command = int(input("Introduceti comanda:"))
                assert command in [1, 2, 3]
                return command

            except (ValueError, AssertionError):
                print("Valoarea introdusa nu este o comanda valida, incercati alta valoare")


    def get_text_input(self, msg=""):
        return input(msg)


    def get_numerical_input(self, msg=""):
        while True:
            try:
                return int(input(msg))
            except ValueError:
                enter("Valoarea introdusa nu este un numar, incercati alta valoare")


    def enter(self, msg=""):
        input(f"{msg}\nPress Enter to continue")

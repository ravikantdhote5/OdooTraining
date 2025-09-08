
#Classes And Objects

class Car:

    def __init__(self, company, model, year):
        self.company = company        # Brand of the car (e.g., Toyota)
        self.model = model      # Model of the car (e.g., Camry)
        self.year = year        # Manufacturing year (e.g., 2024)

    def display_info(self):
        print(f"{self.year} {self.company} {self.model}")

    def start_engine(self):
        print(f"The {self.company} {self.model}'s engine has started.")


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Amaze", 2021)


car1.display_info()
car1.start_engine()

car2.display_info()
car2.start_engine()


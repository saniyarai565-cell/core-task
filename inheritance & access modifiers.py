class Vehicle:
    def _init_(self, brand, model):
        self._brand = brand      # Protected
        self._model = model
        self._speed = 0

    def start(self):
        print(f"{self._brand} {self._model} started.")

    def accelerate(self):
        self._speed += 10
        print(f"{self._brand} {self._model} speed: {self._speed} km/h")

    def stop(self):
        self._speed = 0
        print(f"{self._brand} {self._model} stopped.")


class Car(Vehicle):
    def _init_(self, brand, model, fuel_type):
        super()._init_(brand, model)
        self.__fuel_type = fuel_type  # Private

    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self._model}, Fuel: {self._fuel_type}")
        c1 = Car("Toyota", "Fortuner", "Diesel")
        c1.start()
        c1.accelerate()
        c1.show_details()
        c1.stop()
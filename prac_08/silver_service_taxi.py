from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.50
    number_of_fares = 0

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.current_fare_distance = 0
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                             self.current_fare_distance, self.price_per_km,
                                                             self.flag_fall * self.number_of_fares)

    def start_fare(self):
        self.current_fare_distance = 0
        self.number_of_fares += 1

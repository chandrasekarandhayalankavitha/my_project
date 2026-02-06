
class vehicle:
    def __init__(self,vehicle_id,peak_hour=0):
        self.vehicle_id = vehicle_id
        self.peak_hour = peak_hour
    def calculate_fare(self):
        pass
    def surcharge(self,fare):
        if self.peak_hour == 1:
            fare += fare * 0.25
        return fare

class bus(vehicle):
    def __init__(self,vehicle_id,fare,peak_hour=0):
        super().__init__(vehicle_id,peak_hour)
        self.fare = fare
    def calculate_fare(self):
        total_fare = self.surcharge(self.fare)
        print(f"Bus ID: {self.vehicle_id}, Total Fare: %.2f" % total_fare)

class taxi(vehicle):
    def __init__(self,vehicle_id,distance,rpkm,peak_hour=0):
        super().__init__(vehicle_id,peak_hour)
        self.distance = distance
        self.rateperkm = rpkm
    def calculate_fare(self):
        self.fare = self.distance * self.rateperkm
        total_fare = self.surcharge(self.fare)
        print(f"Taxi ID: {self.vehicle_id}, Total Fare: %.2f" % total_fare)

class metro(vehicle):
    def __init__(self,vehicle_id,zone,rpz,peak_hour=0):
        super().__init__(vehicle_id,peak_hour)
        self.zone = zone
        self.rateperzone = rpz
    def calculate_fare(self):
        self.fare = self.zone * self.rateperzone
        total_fare = self.surcharge(self.fare)
        print(f"Metro ID: {self.vehicle_id}, Total Fare: %.2f" % total_fare)

bus1 = bus("BUS123", 50, peak_hour=0)
bus1.calculate_fare()

taxi1 = taxi("TAXI456", 10, 15, peak_hour=0)
taxi1.calculate_fare()

metro1 = metro("METRO789", 3, 20, peak_hour=1)
metro1.calculate_fare()
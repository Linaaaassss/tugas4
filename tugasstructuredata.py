import queue
import random
import time

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spaces = capacity
        self.queue = queue.Queue()

    def park_vehicle(self, vehicle):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            print(vehicle, "parked. Available spaces:", self.available_spaces)
        else:
            print("Parking lot is full. ", vehicle, "waiting in queue.")
            self.queue.put(vehicle)

    def release_vehicle(self):
        if not self.queue.empty():
            vehicle = self.queue.get()
            print("Releasing", vehicle, "from queue.")
            self.park_vehicle(vehicle)
        else:
            if self.available_spaces < self.capacity:
                self.available_spaces += 1
                print("Parking lot is no longer full. Space available.")

def main():
    parking_lot = ParkingLot(capacity=5)
    vehicles = ["Car", "Motorcycle", "Truck"]

    while True:
        time.sleep(random.uniform(0.5, 2))  # Simulate random arrival time
        vehicle_type = random.choice(vehicles)
        if vehicle_type == "Truck":
            time.sleep(2)  # Trucks take longer to park
        parking_lot.park_vehicle(vehicle_type)
        time.sleep(random.uniform(0.5, 2))  # Simulate random departure time
        parking_lot.release_vehicle()

if __name__ == "__main__":
    main()
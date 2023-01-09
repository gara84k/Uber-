from car import Car
from accountDriver import Driver
from accountUser import User
from route import Router
from payment import Payment

class Trip(Car, Driver, User, Router, Payment):
    idTrip = int
    
    def __init__(self, idTrip, Car, User, Drive, Router, Payment):
        super().__init__(Car, User, Drive, Router, Payment)
        self.idTrip = idTrip
        
   
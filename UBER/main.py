from pprint import pprint
from account import Account
from accountDriver import Driver
from accountUser import User
from car import Car
from payment import Payment
from paymentCard import PaymentCard
from paymentCash import PaymentCash
from paymentTransfer import PaymentTransfer
from route import Router
from trip import Trip
from uberConfort import UberConfort
from uberX import UberX
if __name__ == "__main__":
    #usuario1 =User(1, "Luis Squillo","Masculino",9999999,29)
    #print(vars(usuario1))
    #usuario2 =User(2, "Benito Camelas","Masculino",9999999,29)
    #print(vars(usuario2))
    
    #carro1 = Car("PCH-142", "Chevrolet Corsa", "Gris", 2015, Driver(3, "assd asda"))
    #print(vars(carro1))
    carro2 = UberX("PCF-5599", "Chevrolet Said", "Gris", 2010, "juan Pepe", 9999999, 22, "licencia1")    
    print(vars(carro2))
    carrro3 =UberConfort ("PKF-8962", "Nissan Corola", "Gris", 2003, "Alexander Ortiz", 9999999, 22, "licencia1")    
    print(vars(carrro3))
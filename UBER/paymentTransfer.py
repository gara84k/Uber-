from payment import Payment

class PaymentTransfer(Payment):
    cuenta = int
    banco  = str
    datosTargeta =str
    
    def _init__(self, id, valor, fecha, cuenta, banco, datoTarjeta):
        super().__init__(id, valor, fecha)
        self.cuenta = cuenta
        self.banco  = banco 
        self.datosTargeta = datoTarjeta
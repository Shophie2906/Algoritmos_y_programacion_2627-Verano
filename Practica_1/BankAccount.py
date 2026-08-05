from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, numero_cuenta, nombre_titular, saldo_inicial=0.0):
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self._balance = saldo_inicial
        self.historial_transacciones = []
        
    def deposit(self, amount): # Sumar al balance y registrar en historial
        if amount <= 0:
            print(" El monto a depositar debe ser positivo.")
            return False
        
        self._balance += amount
        self.historial_transacciones.append(f"Deposito: +${amount:.2f}") 
        return True 

    @abstractmethod
    def withdraw(self, amount) -> bool: # Las clases hijas implementaran su regla de retiro
        pass
        
    def show(self):
        print(f" Numero de cuenta: {self.numero_cuenta}")
        print(f" Titular: {self.nombre_titular}")
        print(f" Saldo actual: ${self._balance:.2f}")
        
    def mostrar_historial(self):
        print()
        print("==== ESTADO DE CUENTA ===")
        print()
        self.show()
        
        print(" HISTORIAL DE TRANSACCIONES ")
        print()
        if not self.historial_transacciones:
            print(" No hay movimientos registrados")
        else: 
            for transaccion in self.historial_transacciones:
                print(f" {transaccion}")
        
        
class SavingsAccount(BankAccount):
    def __init__(self, numero_cuenta, nombre_titular, saldo_actual, tasa_interes):
        super().__init__(numero_cuenta, nombre_titular, saldo_actual)
        self.tasa_interes = tasa_interes
        self.tipo = "Ahorros"
    
    def withdraw(self, amount):
        if amount > self._balance:
            print(" La transaccion no puede ser procesada por sobregiro")
            return False
        self._balance -= amount
        self.historial_transacciones.append(f"Retiro: -${amount:.2f}")    
        return True
    
    def show(self):
        super().show()
        print(f" Tasa de Interes: {self.tasa_interes}")
        
    def aplicar_intereses(self):
        monto_interes = self._balance * self.tasa_interes
        self._balance += monto_interes
        self.historial_transacciones.append(f" Interes aplicado ({self.tasa_interes*100:.1f}%): +{monto_interes:.2f}")
        return monto_interes
    
class CheckingAccount(BankAccount):
    def __init__(self, numero_cuenta, nombre_titular, saldo_actual, limite_sobregiro):
        super().__init__(numero_cuenta, nombre_titular, saldo_actual)
        self.limite_sobregiro = limite_sobregiro
        self.tipo = "Corriente"
    
    def withdraw(self, amount):
        if amount > (self._balance + self.limite_sobregiro):
            print(" La transaccion no puede ser procesada por superar el limite establecido")
            return False
        self._balance -= amount
        self.historial_transacciones.append(f"Retiro: -${amount:.2f}")
        return True
      
    def show(self):
        super().show()
        print(f" Limite de Sobregiro: {self.limite_sobregiro}")
        
        
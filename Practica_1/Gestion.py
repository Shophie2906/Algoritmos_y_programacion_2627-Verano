from BankAccount import SavingsAccount, CheckingAccount

class Gestion():
    def __init__(self):
        self.cuentas = []
    
    def Start(self):
        
        while True: 
            print()
            print(" Bienvenido al portal de gestion bancaria!")
            print(" Selecciona una opcion: ")
            print("\t 1- Agregar cuenta bancaria")
            print("\t 2- Realizar depósitos y retiros")
            print("\t 3- Transferir dinero entre cuentas")
            print("\t 4- Consultar estado e historial")
            print("\t 5- Aplicar intereses a cuenta de ahorros")
            print("\t 6- Salir")
            
            opcion = int(input(" Indique su opcion deseada(1-6): "))
            
            if opcion == 1: 
                print()
                self.agregar_cuenta()
            elif opcion == 2:
                print()
                self.movimientos()
            elif opcion == 3:
                print()
                self.transferir()
            elif opcion == 4:
                self.consulta()
            elif opcion == 5:
                self.aplicar_intereses_accion() 
            elif opcion == 6:
                print(" Gracias por elegirnos!") 
                break      
    
    def agregar_cuenta(self):
        print("Que tipo de cuenta desea crear?")
        print("\t 1- Ahorros")
        print("\t 2- Corriente")
        
        try:
            print()
            tipo_cuenta = int(input(" Indique el numero: "))
            
            if tipo_cuenta not in [1, 2]:
                print("Error! Opcion no disponible")
                return
            
            print()
            nombre = input(" Nombre del titular: ").strip()
            numero = input(" Numero de cuenta (6 digitos): ").strip()
            saldo = float(input(" Saldo Inicial: "))
            
            if tipo_cuenta == 1:
                tasa = float(input(" Tasa de interes (eg. 0.02 para 2%): "))
                nueva_cuenta = SavingsAccount(numero, nombre, saldo, tasa)
            
            elif tipo_cuenta == 2:
                limite = float(input(" Limite de sobregiro (eg. 500.0): "))
                nueva_cuenta = CheckingAccount(numero, nombre, saldo, limite)            
            
            self.cuentas.append(nueva_cuenta)
            print()
            print(f" Cuenta {numero} creada con exito!")
    
        except ValueError:
            print("Entrada inválida. Ingrese valores numéricos correctos.")
            
    def movimientos(self):  
        try:
            print()
            # indique su usuario input
            usuario_ingresado = input("Indique su usuario(cedula): ").strip()
            # veirifcar que el usuario coincida con alguno de los guadados
            cuenta = self.buscar_cuenta(usuario_ingresado)
            # error cuenta inexistente
            if cuenta is None:
                print("Cuenta inexistente!")
                return 
                 
            print()
            print(f"Bienvenido al portal {cuenta.nombre_titular}!")
            print("Que deseas hacer hoy?") 
            print("\t 1- Deposito")
            print("\t 2- Retiro") 
            menu = int(input("Indique opcion a relaizar (1-2): "))
            # realizar deposito 1 o retiro 2
            if menu == 1:
                monto = float(input("Monto a depositar: "))
                if monto <= 0:
                    print("Error! Monto invalido")
                    return
                cuenta.deposit(monto)
                print(f" Deposito exitoso! | Saldo de cuenta: ${cuenta._balance:.2f}")
                
            elif menu == 2:
                monto = float(input("Monto a retirar: "))
                if monto <= 0:
                    print("Error! Monto invalido")
                    return
                
                cuenta.withdraw(monto)
                print(f" Retiro exitoso! | Saldo de cuenta: ${cuenta._balance:.2f}")
            
            else:
                print(" Opción invalida.")
            
        except ValueError:
            print("Entrada inválida. Ingrese numero validos.")  
    
    def buscar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None

    def transferir(self):
        try: 
            # ingresar usuario 
            print()
            usuario_emisor = input("Indique su usuario(cedula): ").strip()
            # buscar cuenta (emisor)
            # veirifcar que el usuario coincida con alguno de los guardados
            cuenta_emisor = self.buscar_cuenta(usuario_emisor)
            # error cuenta inexistente
            if cuenta_emisor is None:
                print("Cuenta inexistente!")
                return 
            
            
            print()
            print(f"Bienvenido al portal {cuenta_emisor.nombre_titular}!")
            print(" A continuacion ingresa los datos del receptor: ")
            usuario_receptor = input("Cedula de identidad: ").strip()
            # buscar cuenta x2 (receptor)
            cuenta_receptor = self.buscar_cuenta(usuario_receptor)
            if usuario_receptor == usuario_emisor:
                print("Error! No puede transferir dinero a la misma cuenta")
                return
            
            if cuenta_receptor is None:
                print("Cuenta inexistente!")
                return 
            
            # pedir monto 
            monto_a_transferir = float(input("Monto a Transferir: "))
            if monto_a_transferir <= 0: 
                print("Error! Monto invalido")
                return
    
            # monto a transferir no debe ser sobregiro --> se hace en BankAccout
            if cuenta_emisor.withdraw(monto_a_transferir):
                cuenta_receptor.deposit(monto_a_transferir)
                print(f" Transferencia exitosa a {cuenta_receptor.nombre_titular}! | Saldo de cuenta (emisor): ${cuenta_emisor._balance:.2f}")
                print(f" Recepcion de transferencia exitosa! | Saldo de cuenta actual: ${cuenta_receptor._balance:.2f}")
            
        except ValueError:
            print("Entrada inválida. Ingrese numero validos.")  
        
    def consulta(self):
        try: 
            # ingresar usuario 
            print()
            usuario = input("Indique su usuario(cedula): ").strip()
            # buscar cuenta (emisor)
            # veirifcar que el usuario coincida con alguno de los guardados
            cuenta = self.buscar_cuenta(usuario)
            # error cuenta inexistente
            if cuenta is None:
                print("Cuenta inexistente!")
                return 
            cuenta.mostrar_historial()
            
        except ValueError:
            print("Entrada inválida. Ingrese numero validos.")
    
    def aplicar_intereses_accion(self): 
        print()
        # indique su usuario input
        usuario_interes = input("Indique su usuario(cedula): ").strip()
        # veirifcar que el usuario coincida con alguno de los guadados
        cuenta = self.buscar_cuenta(usuario_interes)
        # error cuenta inexistente
        if cuenta is None:
            print("Cuenta inexistente!")
            return 
        
        if cuenta.tipo != "Ahorros":
            print("Error! La cuenta ingresada es Corriente. Los intereses solo aplican a Cuentas de Ahorros.")
            return   
        
        interes_ganado = cuenta.aplicar_intereses()
        print("Intereses aplicados con exito!")
        print(f" Monto abonado: {interes_ganado:.2f}")
        print(f" Nuevo saldo: {cuenta._balance:.2f}")
        
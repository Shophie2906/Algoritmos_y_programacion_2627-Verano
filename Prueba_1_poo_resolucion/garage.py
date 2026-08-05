
from autos import *
import galeria as db_autos


class Garage:

	def __init__(self):
		self.autos_carrera = []  # Lista global que almacena hasta 4 autos

	def mostrar_estado_autos(self):
		print("\n" + "="*70)
		print("ESTADO ACTUAL DE LA FLOTA DE CARRERAS (MET RACING)")
		print("="*70)
		if not self.autos_carrera:
			print(" No hay autos agregados en el garaje.")
			return

		# Recorrido con índice tradicional mediante range() y len()
		for i in range(len(self.autos_carrera)):
			idx = i + 1
			auto = self.autos_carrera[i]
			
			estado_str = "Encendido" if auto.get_encendido()  else "Apagado"
			compite_str = "SI" if auto.puede_competir() else "NO (Requiere al menos 1 mejora)"
			rpm_motor = auto.get_motor().get_rpm()
			ruedas_str=auto.info_ruedas()
			print(f"[{idx}] {auto.get_marca()} {auto.get_modelo()} | Estado: {estado_str} | Aptitud para competir: {compite_str}")
			print(f"    IP: {auto.get_ip():.2f} | Vmax: {auto.get_vmax():.1f} Km/h | Tmax: {auto.get_tmax():.2f}s | Dmax: {auto.get_dmax():.1f}m")
			print(f"    Sujecion: {auto.get_sujecion():.2f} grips | Potencia: {auto.get_pt():.1f} Hp")
			print(f"    Velocidad Actual: {auto.get_velocidad_actual():.1f} Km/h | RPM Motor: {rpm_motor} RPM")
			print(f"    Mejoras aplicadas -> Motor: {auto.get_motor().get_numero_mejoras()}/ {auto.get_motor().get_max_mejoras()}| Trans: {auto.get_transmision().get_numero_mejoras()}/{auto.get_transmision().get_max_mejoras()} | Carroc: {{auto.get_carroceria().get_numero_mejoras()}}/{auto.get_carroceria().get_max_mejoras()} | Ruedas: {ruedas_str}")
			print("-" * 70)

	def menu_agregar_auto(self):
		if len( self.autos_carrera) >= 4:
			print("\n[!] Se ha alcanzado el límite máximo de 4 autos de carrera en el juego.")
			return

		# Convertimos el diccionario en lista directamente sin usar .keys()
		marcas = list(db_autos.MARCAS_Y_MODELOS)
		print("\n--- Seleccione una Marca ---")
		for i in range(len(marcas)):
			print(f"{i + 1}. {marcas[i]}")
		
		idx_marca = int(input("Seleccione marca: ")) - 1
		marca_sel = marcas[idx_marca]

		modelos = db_autos.MARCAS_Y_MODELOS[marca_sel]
		print(f"\n--- Modelos disponibles de {marca_sel} ---")
		for i in range(len(modelos)):
			print(f"{i + 1}. {modelos[i]}")

		idx_modelo = int (input("Seleccione modelo: ")) - 1
		modelo_sel = modelos[idx_modelo]

		nuevo_auto = AutoCarrera(marca_sel, modelo_sel)
		self.autos_carrera.append(nuevo_auto)
		print(f"\n[+] Auto {marca_sel} {modelo_sel} agregado exitosamente al garaje.")

	def seleccionar_auto(self):
		if not self.autos_carrera:
			print("\n[!] No hay autos disponibles.")
			return None
		print("\n--- Seleccione un Vehículo ---")
		for i in range(len(self.autos_carrera)):
			auto = self.autos_carrera[i]
			print(f"{i + 1}. {auto.get_marca()} {auto.get_modelo()}")
		idx = int(input("Opción: "))- 1
		return self.autos_carrera[idx]

	def menu_agregar_mejora(self):
		auto = self.seleccionar_auto()
		if not auto:
			return

		tipos = ["motor", "transmision", "carroceria", "ruedas"]
		print("\n--- Tipos de Mejora Disponibles ---")
		for i in range(len(tipos)):
			print(f"{i + 1}. Mejora de {tipos[i].capitalize()}")
		while True:
			try:
				idx_tipo = int(input("Seleccione mejora:")) - 1
				tipo_sel = tipos[idx_tipo]
				break
			except ValueError:
					print("Entrada invalida. Ingrese un numero entero valido.")

		exito, mensaje = auto.agregar_mejora(tipo_sel)
		print(f"\n[Resultado]: {mensaje}")

	def get_autos_carrera(self):
		return self.autos_carrera
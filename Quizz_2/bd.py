db={ 
  "pilotos": [ 
    { 
      "id": 1, 
      "nombre": "Juan Perez", 
      "cedula": "V1234567", 
      "telefono": "0412-3456789", 
      "años_experiencia": 5, 
      "tipo_avion": "Boeing 737" 
    }, 
    { 
      "id": 2, 
      "nombre": "Maria Lopez", 
      "cedula": "V8765432", 
      "telefono": "0414-5678901", 
      "años_experiencia": 8, 
      "tipo_avion": "Airbus A380" 
    }, 
    { 
      "id": 3, 
      "nombre": "Carlos Rodriguez", 
      "cedula": "V9876543", 
      "telefono": "0426-7890123", 
      "años_experiencia": 10, 
      "tipo_avion": "Boeing 747" 
    }, 
    { 
      "id": 4, 
      "nombre": "Luisa Gomez", 
      "cedula": "V6543210", 
      "telefono": "0424-5678901", 
      "años_experiencia": 7, 
      "tipo_avion": "Airbus A350" 
    } 
  ], 
  "vuelos": [ 
    { 
      "id": 1, 
      "fecha_salida": "2024-03-01 08:00:00", 
      "lugar_despegue": "Aeropuerto Internacional de Maiquetía Simón Bolívar (CCS)", 
      "destino": "Miami", 
      "id_piloto": 1, 
      "ids_pasajeros": [0,1,2,3,4,5,16] 
    }, 
    { 
      "id": 2, 
      "fecha_salida": "2024-03-02 10:00:00", 
      "lugar_despegue": "Aeropuerto Internacional de La Chinita (MAR)", 
      "destino": "Madrid", 
      "id_piloto": 2, 
      "ids_pasajeros": [6,7,8,9,14,17] 
    }, 
    { 
      "id": 3, 
      "fecha_salida": "2024-03-03 12:00:00", 
      "lugar_despegue": "Aeropuerto Internacional Simón Bolívar (CCS)", 
      "destino": "New York", 
      "id_piloto": 3, 
      "ids_pasajeros": [10,11,12,13,14] 
    }, 
    { 
      "id": 4, 
      "fecha_salida": "2024-03-04 14:00:00", 
      "lugar_despegue": "Aeropuerto Internacional de La Chinita (MAR)", 
      "destino": "Roma", 
      "id_piloto": 4, 
      "ids_pasajeros": [15,16,17,5,7,0] 
    } 
  ], 
  "pasajeros": [ 
    { 
      "id": 0, 
      "nombre": "Pedro Gomez", 
      "cedula": "V12345678", 
      "telefono": "0416-1234567", 
      "millas_vuelo": 2500, 
      "confirmado": False 
    }, 
    { 
      "id": 1, 
      "nombre": "Ana Martinez", 
      "cedula": "V23456789", 
      "telefono": "0426-2345678", 
      "millas_vuelo": 1500, 
      "confirmado": False 
    }, 
       { 
      "id": 2, 
      "nombre": "Sofia Hernandez", 
      "cedula": "V45678901", 
      "telefono": "0414-4567890", 
      "millas_vuelo": 1800, 
      "confirmado": False 
    }, 
    { 
      "id": 3, 
      "nombre": "Luisa Castro", 
      "cedula": "V56789012", 
      "telefono": "0424-5678901", 
      "millas_vuelo": 2200, 
      "confirmado": False 
    }, 
    { 
      "id": 4, 
      "nombre": "Diego Perez", 
      "cedula": "V67890123", 
      "telefono": "0416-6789012", 
      "millas_vuelo": 2800, 
      "confirmado": False 
    }, 
 
    { 
      "id": 5, 
      "nombre": "Elena Gutierrez", 
      "cedula": "V78901234", 
      "telefono": "0426-7890123", 
      "millas_vuelo": 3000,  
      "confirmado": False 
    }, 
    { 
      "id": 6, 
      "nombre": "Andres Rodriguez", 
      "cedula": "V89012345", 
      "telefono": "0412-8901234", 
      "millas_vuelo": 3200, 
      "confirmado": False 
    }, 
    { 
      "id": 7, 
      "nombre": "Martha Diaz", 
      "cedula": "V90123456", 
      "telefono": "0416-9012345", 
      "millas_vuelo": 1800, 
      "confirmado": False 
    }, 
    { 
      "id": 8, 
      "nombre": "Roberto Fernandez", 
      "cedula": "V01234567", 
      "telefono": "0424-0123456", 
      "millas_vuelo": 2000, 
      "confirmado": False 
    }, 
    { 
      "id": 9, 
      "nombre": "Laura Suarez", 
      "cedula": "V11234568", 
      "telefono": "0412-1234567", 
      "millas_vuelo": 1400, 
      "confirmado": False 
    }, 
{ 
      "id":10, 
      "nombre": "Javier Garcia", 
      "cedula": "V12234569", 
      "telefono": "0426-2345678", 
      "millas_vuelo": 1600, 
      "confirmado": False 
    }, 
       { 
      "id": 11, 
      "nombre": "Carmen Hernandez", 
      "cedula": "V13234560", 
      "telefono": "0414-3456789",  
      "millas_vuelo": 1900, 
      "confirmado": False 
    }, 
    { 
      "id": 12, 
      "nombre": "Miguel Torres", 
      "cedula": "V14234561", 
      "telefono": "0416-4567890", 
      "millas_vuelo": 2200, 
      "confirmado": False 
    }, 
    { 
      "id": 13, 
      "nombre": "Alejandra Perez", 
      "cedula": "V15234562", 
      "telefono": "0424-5678901", 
      "millas_vuelo": 2400, 
      "confirmado": False 
    }, 
    { 
      "id": 14, 
      "nombre": "Raul Martinez", 
      "cedula": "V16234563", 
      "telefono": "0412-6789012", 
      "millas_vuelo": 2700, 
      "confirmado": False 
    }, 
    { 
      "id": 15, 
      "nombre": "Isabella Suarez", 
      "cedula": "V17234564", 
      "telefono": "0426-7890123", 
      "millas_vuelo": 3100, 
      "confirmado": False 
    }, 
    { 
      "id": 16, 
      "nombre": "Lucia Garcia", 
      "cedula": "V18234565", 
      "telefono": "0412-1234567", 
      "millas_vuelo": 2900, 
      "confirmado": False 
    }, 
    { 
      "id": 17, 
      "nombre": "Roberto Diaz",  
      "cedula": "V19234566", 
      "telefono": "0416-2345678", 
      "millas_vuelo": 2600, 
      "confirmado": False 
    } 
  ] 
} 
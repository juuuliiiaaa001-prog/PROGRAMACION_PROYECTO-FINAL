# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:51:08 2026

@author: Usuario
"""
import json, string, random
from datetime import datetime, timedelta
from Interfaz import colores, ilustracion

mesas = [ 
    {"id": 1,"capacidad": 2, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
          {"id": 2,"capacidad": 2, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
             {"id": 3,"capacidad": 2, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
                {"id": 4,"capacidad": 4, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
                    {"id": 5,"capacidad": 4, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
                        {"id": 6,"capacidad": 2, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
                            {"id": 7,"capacidad": 2, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
                                {"id": 8,"capacidad": 4, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
                                {"id": 9,"capacidad": 4, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
                                {"id": 10,"capacidad": 2, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""},
                                  {"id": 11,"capacidad": 8, "Fecha": "","Hora_Ent": "","Hora_Sal": "","Duración": "","Codigo": ""}
                                    ]

try:

 with open("registro.json", "r") as rg:
     load = json.load(rg)
except(json.JSONDecodeError, FileNotFoundError):
    load=[]



Reservaciones = load.copy()

#Cantidad de reservas
Cant_reserv = len(Reservaciones)

def liberar_mesas():

    global Reservaciones

    dia_actual = datetime.now().strftime("%Y-%m-%d")
    hora_actual = datetime.now().strftime("%H:%M")

    Reser_Pas_D = []
    Reser_Pas_H = []
    if Cant_reserv != 0:

        for i in range(Cant_reserv):
            if ((Reservaciones[i]["Fecha"] <= dia_actual) == True):
                Reser_Pas_D.append(Reservaciones[i])
        for i in range(len(Reser_Pas_D)):
            if (Reser_Pas_D[i]["Hora_Ent"] < hora_actual):
                Reser_Pas_H.append(Reser_Pas_D[i])
    
        for i in range(len(Reser_Pas_H)):

            ReserPas = Reser_Pas_H[i]["Hora_Ent"]
            Reservaciones = [reser for reser in Reservaciones if reser["Hora_Ent"] >= ReserPas ]
    
        return Reservaciones

def mostrar_mesas_disponibles():
    
    liberar_mesas()

    fechaocupada = []
    horaocupada = []
    disponibles = mesas.copy()

    #El usuario elige la fecha de la reserva

    while True:
        fecha = input("¿Para qué fecha reservarás? (formato AÑO-MES-DIA, ejemplo 2026-06-02)\n")

        try:
            fecha_valida = datetime.strptime(fecha, "%Y-%m-%d")

            break
        except ValueError:
            print("Formato inválido. Usa AAAA-MM-DD.")

    for i in range(Cant_reserv):
        
        FechaOcp = (Reservaciones[i]["Fecha"] == fecha)
        if FechaOcp == True:
            fechaocupada.append(Reservaciones[i])

    while True:

        # El usuario elige la hora de llegada
        hora_str = input("¿A qué hora llegas? (formato HH:MM, ejemplo 14:30): ")
    
        try:
            hora_llegada = datetime.strptime(hora_str, "%H:%M")
            break
        except ValueError:
            print("Formato de hora inválido.")
    
    for i in range(len(fechaocupada)):

        HoraOcp = (fechaocupada[i]["Hora_Ent"] == hora_str)
        if HoraOcp == True:
            horaocupada.append(fechaocupada[i])
            
    #Eliminamos la mesa ocupada
    for i in range(len(horaocupada)):
        mesaocupada = horaocupada[i]["id"]
        disponibles = [mesa for mesa in disponibles if mesa["id"] != mesaocupada]


    print("\n--- Mesas disponibles ---")
    
    if not disponibles:
        print("No hay mesas disponibles en este momento.")
        return [], fecha, hora_str
    
    for i in range(len(disponibles)):
        print(f"Mesa {disponibles[i]['id']} - Capacidad: {disponibles[i]['capacidad']} personas")

    RED, GREEN, YELLOW, RESET = colores()

    a, color = ilustracion()

    for i in range(len(disponibles)):
        mesa = disponibles[i]["id"]
        color.replace(mesa, GREEN)
        
    print(a)
    print("Verde: Disponible, Rojo: Ocupada, Amarillo: Barra libre")

    return disponibles, fecha_valida, hora_str, hora_llegada

def generar_codigo():

    codigo = ''.join(random.choices(
        string.ascii_uppercase + string.digits,
        k=6
    ))

    return codigo

def hacer_reservacion():

    reserva = []

    #El usuario elige la cantidad de personas
    while True:
        try:
            num_personas = int(input("¿Para cuantas personas?\n"))
            break
        except:
            print("Ingresar numeros enteros")

    disponibles, fecha_valida, hora_str, hora_llegada = mostrar_mesas_disponibles()
        
    while True:
        id_elegida = int(input("\n¿Qué número de mesa deseas? "))

        for i in range(len(disponibles)):
            mesa = (disponibles[i]["id"] == id_elegida)
            if mesa == True:
                reserva.append(disponibles[i])

        print(reserva)        

        asientos = disponibles[id_elegida - 1]["capacidad"]

        PersonasSinRegistrar = num_personas - asientos

        for i in range(len(reserva)):
            reserva[i]["Fecha"]    = str(fecha_valida.strftime("%Y-%m-%d"))
            reserva[i]["Hora_Ent"] = hora_str
            reserva[i]["Codigo"]   = generar_codigo()
        
        print(reserva)
        if PersonasSinRegistrar <= 0:
            break

        print(f"Cantidad de personas sin asiento {PersonasSinRegistrar}")
        print("Selecciona una mesa más")

        num_personas -= PersonasSinRegistrar 

    mesa = next((m for m in disponibles if m["id"] == id_elegida), None)
    if not mesa:
        print("Mesa no válida.")
        return

    # Duración fija de la reservación: 2 horas
    duracion = int(input("¿Cuántas horas durará tu visita? (1-4): "))
    if not 1 <= duracion <= 4:
        print("Duración no válida.")
        return

    hora_salida = hora_llegada + timedelta(hours=duracion)
    hora_salida_str =  datetime.strftime(hora_salida, "%H:%M")

    for i in range(len(reserva)):
        reserva[i]["Hora_Sal"] = hora_salida_str
        reserva[i]["Duración"] = duracion
    
    print(reserva)
    
    Reservaciones.extend(reserva)

    print(Reservaciones)

    with open("registro.json", "w") as rg:
      json.dump(Reservaciones, rg )

    for i in range(len(reserva)):
        codigo = reserva[i]["Codigo"]
        mesa = reserva[i]["id"]
        capacidad =  reserva[i]["capacidad"]

        print("\nreservación completa")
        print(f"  Mesa {mesa} - Capacidad: {capacidad} personas")
        print(f"  Llegada: {hora_str}")
        print(f"  Salida:  {hora_salida_str}")
        print(f"  Codigo:  {codigo}")

    reserva.clear()

def cancelar_reservación():

    global Reservaciones

    print("Hola buenas")
    Deseo = input("¿Deseas cancelar tu reservación?\n").lower()
    if Deseo == "si":
        Codigo = input("¿Cuál es tu codigo de acceso?\n").upper()
        for i in range(Cant_reserv):
          
         Reservaciones = [reser for reser in Reservaciones if reser["Codigo"] != Codigo]
    
    with open("registro.json", "w") as rg:
        json.dump(Reservaciones, rg)

    print("Reservación cancelada")

    return Reservaciones


def menu():
    while True:
        print("\n=== Sistema de Reservaciones ===")
        print("1. Hacer reservación")
        print("2. Ver mesas disponibles")
        print("3. Cancelar reservación")
        print("4. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            hacer_reservacion()
        elif opcion == "2":
            mostrar_mesas_disponibles()
        elif opcion == "3":
            cancelar_reservación()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    menu()

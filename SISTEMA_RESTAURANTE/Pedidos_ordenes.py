# --- SISTEMA DE TICKETS Y ORDENES ---

# Importacion de datos:

import json 
import os
from datetime import datetime
from Menu import Portada, Desayunos, Comidas, Bebidas, Bebidas_alcoholicas, Postres, Despedida
from Interfaz import ilustracion

# Carga de base de datos JSON:

try: 
    with open("registro.json", "r") as rg:
        load = json.load(rg)
except(json.JSONDecodeError, FileNotFoundError):
    load=[]

Reservaciones = load.copy()

# Ordenes y reservaciones:

historial_pedidos = []
contador_pedidos = 1

paginas_menu = [Desayunos, Comidas, Bebidas, Bebidas_alcoholicas, Postres]

menu_completo = {}
for p in paginas_menu:
    menu_completo.update(p.menu)

def buscar_reservacion_por_codigo(codigo_usuario):

    from Reservaciones import Reservaciones
    for res in Reservaciones:
        if res["Codigo"].upper() == codigo_usuario.upper():
            return res
    return None

def registrar_nueva_orden():
    global contador_pedidos
    carrito = []

    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print(" --- REGISTRAR NUEVA ORDEN ---")
    print("=" * 40)

    tiene_reserva = input("\n¿El cliente cuenta con reservacion? (S/N): ").strip().lower()
    info_reserva = None

    if tiene_reserva == 's':
        codigo = input("ingrese el codigo de reservacion: ").strip()
        info_reserva = buscar_reservacion_por_codigo(codigo)
        if info_reserva:
            nombre_cliente = f"Cliente reserva (Mesa {info_reserva['id']})"
            print(f" Codigo valido para Mesa {info_reserva['id']}")
        else:
            print("Codigo de reservacion no encontrado")
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
    else:
        nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
    
    if not nombre_cliente:
        nombre_cliente = "General"

# Pedido:



    print("\n--- Ingrese los productos ('FIN' para terminar) ---")
    while True:
        producto_input = input("Producto: ").strip()

        if producto_input.upper() == 'FIN':
            break

        if producto_input in menu_completo and menu_completo[producto_input] != "":
            try:
                cantidad = int(input(f"¿Cuantas unidades de '{producto_input}' desea agregar?:  "))
                if cantidad <= 0:
                    raise ValueError
            except ValueError:
                print("Cantidad debe ser un numero positivo.")
                cantidad = 1
        
            precio = menu_completo[producto_input]
            carrito.append({
                "producto": producto_input,
                "precio": precio,
                "cantidad": cantidad
            })
            print(f" Añadido: {cantidad}*{producto_input}")
        else:
            print(f" El producto '{producto_input}' no se encuentra en el menu.")

# --- HISTORIAL ---

    if carrito:
        total = sum(item['precio'] * item['cantidad'] for item in carrito)
        nueva_orden = {
            "id": contador_pedidos,
            "cliente": nombre_cliente,
            "items": carrito,
            "total": total,
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prioridad": "Alta" if info_reserva else "Normal",
            "despachado": False
        }

        historial_pedidos.append(nueva_orden)
        print(f"\n Ordden #{contador_pedidos} registrada exitosamente.")
        contador_pedidos += 1
    else:
        print("\n No se han agregado productos. Orden no registrada.")
    input("\n[Enter] para continuar...")

def imprimir_ticket_consola(orden):
    ancho_ticket = 40
    os.system('cls' if os.name == 'nt' else 'clear')

    print("*" * ancho_ticket)
    print("--- TICKET DE ORDEN ---")
    print("*" * ancho_ticket)
    print(f"Folio de orden: {orden['id']}")
    print(f"Fecha/hora:     {orden['fecha_hora']}")
    print(f"cliente:        {orden['cliente']}")
    print(f"Prioridad:      {orden['prioridad']}")
    print(f"Estado:         {'Despachado' if orden['despachado'] else 'En preparación'}")
    print("-" * ancho_ticket)

    for item in orden['items']:
        subtotal = item['precio'] * item['cantidad']
        nombre_prod = f"{item['cantidad']}x {item['producto']}"
        espacio = ancho_ticket - len(nombre_prod)
        print(f"{nombre_prod}{str(f'${subtotal:.2f}'):>{espacio}}")

    print("-" * ancho_ticket)
    total_str = f"TOTAL: ${orden['total']:.2f}"
    print(f"{total_str:>{ancho_ticket}}")
    print(" ¡Gracias por su compra!")
    print("*" * ancho_ticket)

def administrar_ordenes_y_tickets():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- ADMINISTRACION DE ORDENES ---")
        print("1. Registrar nueva orden")
        print("2. Ver historial de ordenes")
        print("3. Marcar como despachado")
        print("4. Volver al menu principal")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            registrar_nueva_orden()

        elif opcion == "2":
            if not historial_pedidos:
                print("\nNo hay ordenes registradas.")
                input("\n[Enter] para continuar...")
                continue

            print("\n--- HISTORIAL DE ORDENES ---")

            ordenes_ordenadas = sorted(historial_pedidos, key=lambda x: x['fecha_hora'], reverse=True)
            for o in ordenes_ordenadas:
                estado = " Despachado " if o['despachado'] else "En preparación"
                print(f"Folio: #{o['id']} | Cliente: {o['cliente']} | Total: ${o['total']:.2f} | Estado: {estado} | Prioridad: {o['prioridad']}")
                
            folio_ticket = input("\nIngrese el folio de la orden para imprimir ticket (o '0' para volver): ").strip()
            if folio_ticket.isdigit():
                orden_encontrada = next((o for o in historial_pedidos if str(o['id']) == folio_ticket), None)
                if orden_encontrada:
                    imprimir_ticket_consola(orden_encontrada)
                else:
                    print("Folio no encontrado.")
                    input("\n[Enter] para continuar...")
        elif opcion == "3":
            if not historial_pedidos:
                print("\nNo hay ordenes registradas.")
                input("\n[Enter] para continuar...")
                continue

            folio_despacho = input("\nIngrese el folio de la orden para marcar como despachada (o '0' para volver): ").strip()
            if folio_despacho.isdigit():
                orden_encontrada = next((o for o in historial_pedidos if str(o['id']) == folio_despacho), None)
                if orden_encontrada:
                    orden_encontrada['despachado'] = True
                    print(f"Orden #{orden_encontrada['id']} marcada como despachada.")
                else:
                    print("Folio no encontrado.")
            else:
                print("Entrada no valida.")
            input("\n[Enter] para continuar...")
            
        elif opcion == "4":
            break
def sistema_restaurante():

    paginas = [Portada, Desayunos, Comidas, Bebidas, Bebidas_alcoholicas, Postres, Despedida]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SISTEMA DE RESTAURANTE ===")
        print("1. Ver menu")
        print("2. Reservaciones")
        print("3. Administrar ordenes y tickets")
        print("4. Salir")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            for p in paginas:
                p.mostrar_como_pagina()
        elif opcion == "2":
            menu()
        elif opcion == "3":
            administrar_ordenes_y_tickets()
        elif opcion == "4":
            print("\n¡Buen dia!")
            break
            
if __name__ == "__main__":
    administrar_ordenes_y_tickets()
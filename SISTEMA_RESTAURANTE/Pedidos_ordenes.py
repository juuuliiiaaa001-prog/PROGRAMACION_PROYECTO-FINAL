# --- SISTEMA DE TICKETS Y ORDENES ---

# Importacion de datos:

import json 

import os

from datetime import datetime

from Menu import Portada, Desayunos, Comidas, Bebidas, Bebidas_alcoholicas, Postres, Despedida

from Reservaciones import Reservaciones


historial_pedidos = []
contador_pedidos = 1

paginas_menu = [Desayunos, Comidas, Bebidas, Bebidas_alcoholicas, Postres]

menu_completo = {}
for p in paginas_menu:
    menu_completo.update(p.menu)

def buscar_reservacion_por_codigo(codigo_usuario):
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


# --- FORMATO DEL MENU ---
import os # importa el modulo para limpiar la consola

class Cafeteria:
    def __init__(self, nombre_pagina): #asigna valores a los atributos de la clase
        self.nombre_pagina = nombre_pagina # guarda el titulo de la pagina
        self.menu = {} # diccionario para guardar los items del menu y sus precios

# Agregar items al menu

    def add_item(self, item, precio): # agrega un item al menu con su precio
        self.menu[item] = precio # asigna el precio al item en el diccionario

    def add_subseccion (self, subtitulo): # agrega un subtitulo al menu sin precio
        self.menu[subtitulo] = "" # asigna None al subtitulo en el diccionario

    def add_subsubseccion(self, subsubtitulo): # agrega un subsubtitulo al menu sin precio
        self.menu[subsubtitulo] = "" 
    
    def mostrar_como_pagina(self): # muestra el menu como una pagina
        os.system('cls') # limpia la consola

# Tamaño de pagina:

        ancho_total = 40 # define el ancho total de la pagina
        max_lineas = 20 # define el numero maximo de lineas que se pueden imprimir en una pagina
        lineas_impresas = 0 # contador

# Encabezado:

        print(f"\n" + "="*ancho_total)
        print(f"{self.nombre_pagina.center(ancho_total)}")
        print("="*ancho_total + "\n")
        lineas_impresas += 4 

        for item, precio in self.menu.items():
            if precio == "":
                print(f"\n\033[1;36m{item}\033[0m") 
                lineas_impresas += 2
            else:
                espacio = ancho_total - len(str(item))
                print(f"{item}{str(f'${precio}'):>{espacio}}")
                lineas_impresas += 1

# Espacio en blanco:

        while lineas_impresas < max_lineas:
            print("")
            lineas_impresas += 1
        
        print("\n" + "=" * ancho_total)
        input("\n[Enter] para continuar...")

# --- CONFIGURACION DE PAGINAS ---

# PAGINA 1: PORTADA
Portada = Cafeteria("¡BIENVENIDO A NUESTRO RESTAURANTE!") 
Portada.add_subseccion(" Elisea ")

# PAGINA 2: DESAYUNOS

Desayunos = Cafeteria("DESAYUNOS")
Desayunos.add_item("Chilaquiles", 160)
Desayunos.add_item("Enchiladas", 160)
Desayunos.add_item("Wafles", 160)
Desayunos.add_item("Hot Cakes", 160)

# PAGINA 3: COMIDAS

Comidas = Cafeteria("COMIDAS")
Comidas.add_item("Hamburguesa", 200)
Comidas.add_item("Pizza individual", 160)
Comidas.add_item("Pizza familiar", 300)
Comidas.add_item("Tacos (Ordem de cinco tacos)", 200)

# PAGINA 4: BEBIDAS (SIN ALCOHOL)

Bebidas = Cafeteria("BEBIDAS (SIN ALCOHOL)")
Bebidas.add_subseccion("Cafe de especialidad: ")
Bebidas.add_item("Expresso", 70)
Bebidas.add_item("Americano", 70)
Bebidas.add_item("Cappuccino", 120)
Bebidas.add_item("Latte", 120)
Bebidas.add_item("Mocha", 120)

Bebidas.add_subseccion("Tés: ")
Bebidas.add_item("Té verde", 70)
Bebidas.add_item("Matcha", 120)

Bebidas.add_subseccion("Jugos naturales: ")
Bebidas.add_item("Naranja", 70)
Bebidas.add_item("Toronja", 70)

# PAGINA 5: BEBIDAS ALCOHOLICAS

Bebidas_alcoholicas = Cafeteria("BEBIDAS ALCOHOLICAS")
Bebidas_alcoholicas.add_subseccion("Cervezas Artesanales: ")
Bebidas_alcoholicas.add_item("Pale Ale", 60)
Bebidas_alcoholicas.add_item("India Pale Ale", 60)
Bebidas_alcoholicas.add_item("Stout", 60)
Bebidas_alcoholicas.add_item("Porter", 60)
Bebidas_alcoholicas.add_item("Lager", 60)

Bebidas_alcoholicas.add_subseccion("Vinos: ")
Bebidas_alcoholicas.add_item("Tinto", 900)
Bebidas_alcoholicas.add_item("Blanco", 900)
Bebidas_alcoholicas.add_item("Rosado", 900)

Bebidas_alcoholicas.add_subseccion("Cocteles: ")
Bebidas_alcoholicas.add_item("Margarita", 160)
Bebidas_alcoholicas.add_item("Mojito", 160)
Bebidas_alcoholicas.add_item("Piña Colada", 160)
Bebidas_alcoholicas.add_item("Cosmopolitan", 160)
Bebidas_alcoholicas.add_item("Bloody Mary", 160)

# PAGINA 6: POSTRES

Postres = Cafeteria("POSTRES")
Postres.add_item("Pastel de chocolate", 200)
Postres.add_item("Cheesecake", 200)
Postres.add_item("Tiramisú", 200)
Postres.add_item("Pavlova", 200)

# PAGINA 7: DESPEDIDA

Despedida = Cafeteria("¡GRACIAS POR VISITARNOS!")

# --- EJECUCION  DEL MENU DE PAGINAS ---

paginas = [Portada, Desayunos, Comidas, Bebidas, Bebidas_alcoholicas, Postres, Despedida]

for p in paginas:
    p.mostrar_como_pagina()

os.system('cls' if os.name == 'nt' else 'clear')
print("¡VUELVA PRONTO!")

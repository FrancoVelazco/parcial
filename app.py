import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Auto - 1000 km
         2 - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo.
    2- Kilometraje promedio de los autos.
    3- Precio promedios de todos los servicios.
    4- Informar los kilometrajes que superan el promedio (total).
    5- Informar los kilometrajes que NO superan el promedio (total).
    6- Informar la cantidad de vehiculos de cada tipo.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de cada servicio realizado.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = ["auto", "camioneta", "moto", "camioneta", "auto", "moto"]
        self.lista_marca_vehiculo = [15, 22, 430, 10, 1, 200.20]

    def btn_agregar_on_click(self):
        #  Tipo de vehiculo (auto, camioneta, moto)
        #  Kilometros. ( != 0 )
        while True:
            vehiculo = prompt("Toma de datos", "Ingrese el tipo de vehiculo")
            while (not vehiculo or not vehiculo.isalpha()) or vehiculo != "auto" and vehiculo != "camioneta" and vehiculo != "moto":
                vehiculo = prompt("Toma de datos", "re-ingrese el tipo de vehiculo ")

            kilometros = prompt("Toma de datos", "Ingrese los kilometros del vehiculo")

            kilometros_valido = False
            contador_puntos = 0

        
            if kilometros:
                for valor in kilometros:
                    if not valor.isdigit() and valor != '.':
                        kilometros_valido = False
                        break
                    elif valor == ".":
                        contador_puntos += 1
                        if contador_puntos > 1:
                            kilometros_valido = False
                            break
                    else:
                        kilometros_valido = True

                if kilometros_valido and float(kilometros) != 0:
                    kilometros = float(kilometros)
                else:
                    kilometros_valido = False

                if kilometros_valido:
                    txt = "Los kilometros es valido"
                    self.lista_tipo_vehiculo.append(vehiculo)
                    self.lista_marca_vehiculo.append(kilometros)
                else:
                    txt = "Los kilometros no es valido"
                
                alert("Validación", txt)

                

            continuar = question("Titulo", "¿Desea continuar?")
            if not continuar:
                break

    
    def btn_mostrar_on_click(self):
        # listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
        i = 0
        for vehiculo in self.lista_tipo_vehiculo:
            print(f"{i} - {vehiculo} - {self.lista_marca_vehiculo[i]}km")

            i+= 1


    def btn_informar_on_click(self):
       
        #4- Informar los kilometrajes que superan el promedio (total).
        #5- Informar los kilometrajes que NO superan el promedio (total).
        promedio = 0
        acumulador_kilometros = 0
        for kilometros in self.lista_marca_vehiculo:
            acumulador_kilometros += kilometros
        
        promedio = acumulador_kilometros / len(self.lista_tipo_vehiculo)
        print(f"El promedio es de: {promedio}")

        for kilometros in self.lista_marca_vehiculo:
            if kilometros > promedio:
                print(f"{kilometros} SI SUPERA el promedio")
            elif kilometros < promedio:
                print(f"{kilometros} NO SUPERA el promedio")


       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()

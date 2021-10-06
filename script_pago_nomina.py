"""
La empresa yabadabadu necesita con urgencia pagar la nomina de sus empleados tal como acostumbra 
cada viernes pero justo hoy la plataforma tecnológica se ha visto comprometida por un fallo en uno de 
sus servidores por lo que no cuentan con el sistema principal que usan para tal fin. por esta razón se d
esea leer un archivo plano que posee una lista de los empleados junto al sueldo base de cada uno, usted 
como soporte de sistemas no se encuentra en la empresa pero se le ha dado la tarea de desarrollar un 
script en python que pueda correr en el servidor via ssh para lograr el objetivo se necesita:

Desarrollar un script que permita realizar lo siguiente: 

1) Reciba dos parámetros por terminal, ejemplo:
script_pago_nomina.py [bono1] [bono2]
[Bono 1] Bono General = 5%
[Bono 2] Bono Eficiencia = 15% (Empleados que tengan mas de 5 horas extras en la semana)

2) Leer el archivo llamado nomina.txt
3) Realizar las operaciones pertinentes para cada empleado
4) Guardar el archivo con el monto a pagar en otro archivo llamado pago_nomina_12sep2021.py 
5) Aprovechando la coyuntura se pide cambiar la fecha de ingreso al formato 'YYYY-MM-DD' Ejemplo 23/04/1990 cambiar a 1990-04-23

Archivo nomina.txt
cedula fecha_ingreso empleado sueldo_base horas_extra
1334521 23/12/1999 Juan Castro 60$ 5
12333444 12/12/2012 Carolina Buitriago 90$ 3
13334434 12/12/2012 Julio Castillo 100$ 15
1334523 23/12/1999 Juana archila 160$ 5
12333444 12/12/2012 Daniel Burgos 90$ 3
13334434 12/12/2012 Cesar Guzman 100$ 15
13345266 23/12/1999 Darielsys Maduro 60$ 5
12333474 12/12/2012 Nestor Tovar 90$ 3
13334484 12/12/2012 Carolys Suniaga 100$ 15
13345213 23/12/1999 Hector Gomez 60$ 5
12333444 12/12/2012 Carolina Vargas 90$ 3
13334111 12/12/2012 Julio Mujica 100$ 15
13334456 12/12/2012 Jonh Chancellor 100$ 15
"""

archivo_original = "nomina.txt"
archivo_nomina = "pago_nomina_12sep2021.py"

#1) Recibir los parametros:
#Importar el paquete sys:
import sys

#Leer los argumentos, el argv[0] es el nombre del script:
if (len(sys.argv)<3):
	print("\nFaltan los parametros de bono:\nSintaxis:    script_pago_nomina.py [bono1] [bono2]\n\n")
	quit()

#Leer los porcentajes de la linea de comando:
p_bono1 = sys.argv[1]
p_bono2 = sys.argv[2]

#2) Leer el archivo nomina.txt, se guarda en un arreglo llamado lineas:
with open(archivo_original) as f:
    lineas = f.readlines()
    f.close()

#La linea 1 no va:
del lineas[0]

#3) Realizar las operaciones indicadas para cada empleado:
#Recorrer el arreglo para ejecutar cada uno, separando los campos:
listado = ["cedula fecha_ingreso empleado sueldo_base horas_extra bono1 bono2 total"] #Para el listado de salida
for linea in lineas:
	empleado      = linea.split(sep=" ")
	cedula        = empleado[0]
	fecha_ingreso = empleado[1]
	nombre        = empleado[2]
	apellido      = empleado[3]
	sueldo        = empleado[4]
	horas_extra   = empleado[5]

	sueldo = int(sueldo.replace("$","")) #Convertir el sueldo a valor, quitando antes el dolar ($)
	horas_extra = int(horas_extra)       #Convertir las horas extra a valor

	bono1 = float(sueldo) * float(p_bono1) / 100   #Calcular el bono1
	bono2 = 0

	if (horas_extra > 5):
		bono2 = float(sueldo) * float(p_bono2) / 100   #Calcular el bono2 en base a si se tiene mas de 5 horas extras semanales

	total = float(sueldo) + bono1 + bono2

	fi = fecha_ingreso.split(sep="/")  #Separar las fechas en dia/mes/ano para reconvertir

	fecha_ingreso = fi[2] + "-" + fi[1] + "-" + fi[0]    #Conversion de la fecha a yyyy-mm-dd

	listado.append(cedula + " " + fecha_ingreso + " " + nombre + " " + apellido + " " + str(sueldo) + "$ " + str(bono1) + "$ " 
		+ str(bono2) + "$ " + str(total) + "$")

#Finalmente se guarda la lista resultante en el archivo pago_nomina_12sep2021.py:

with open(archivo_nomina,"w+") as f:
	for empleado in listado:
		f.write(empleado + "\n")
	f.close()

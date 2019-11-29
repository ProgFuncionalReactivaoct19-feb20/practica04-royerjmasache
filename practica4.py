"""
	Práctica 4
	@royerjmasache
"""
# Importación de librerías
import codecs
import json
# Lectura de archivos con uso de codecs y json
file = codecs.open("data/datos.txt")
lines = file.readlines()
linesDictionary = [json.loads(a) for a in lines]
# Uso de filter y función anónima para evaluar la condición requerida y filtrar los resultados
goals = list(filter(lambda a: list(a.items())[1][1] > 3, linesDictionary))
# Presentación de resultados en forma de lista
print("Players with more than 3 goals scored:\n", list(goals))
# Uso de filter y función anónima para cumplir evaluar la condición requerida y filtrar los resultados
country = list(filter(lambda a: list(a.items())[0][1] == "Nigeria", linesDictionary))
# Presentación de resultados en forma de lista
print("Nigeria players:\n", list(country))
# Uso de función anónima para seleccionar la posición
height = lambda a: list(a.items())[2][1]
# Uso de función min, map para la iteración y presentación de resultados en forma de lista
print("Minimum height:\n", min(list(map(height, linesDictionary))))
# Uso de función max, map para la iteración y presentación de resultados en forma de lista
print("Maximum height:\n", max(list(map(height, linesDictionary))))

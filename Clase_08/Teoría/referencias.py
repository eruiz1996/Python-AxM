# PIB nominal en MDD
# fuente: https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_PIB_(nominal)
PIB = {
	'EUA':26_949_643,
	'China':17_700_899,
	'Unión Europea':16_641_391,
	'Alemania':4_429_838,
	'Japón':4_230_862,
	'Mundo':104_476_432
}


# lenguajes de programación
lenguajes = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# sueldos promedio en miles de dólares
sueldos = [56, 55, 57, 63, 52]
# fuente: https://www.hostinger.mx/tutoriales/sueldo-desarrolladores-web

def crear_diccionario(lista1, clave1, lista2, clave2):
	""" crea un diccionario a partir de las listas y claves dadas """
	diccionario = {
		clave1:lista1,
		clave2:lista2
	}
	return diccionario
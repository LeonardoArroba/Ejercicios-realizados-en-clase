usuario = ("zancrow", "1864", "zancrow186@gmail.com")
materias = ["Python", "C++", "vs code", "POO"]
estudiante = {"nombre": "Andres", "edad": 18, "fac": "faci"}
print(usuario[0], materias[1], estudiante["nombre"])
print(usuario[0:2], estudiante.keys(), estudiante.values())
materias.append("Estructura de datos")
estudiante["sexo"], estudiante["edad"] = "M", 18
print(materias, estudiante)
tupla, lista, diccionario = (), [], {}

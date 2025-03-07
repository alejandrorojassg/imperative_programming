#this is my code...
tareas = []  
def agregar_tarea(nombre):
    tareas.append({"nombre": nombre, "completada": False})

def completar_tarea(indice):
    if indice < len(tareas):
        tareas[indice]["completada"] = True

def mostrar_tareas():
    for i, tarea in enumerate(tareas):
        estado = "✓" if tarea["completada"] else "✗"
        print(f"{i+1}. [{estado}] {tarea['nombre']}")

# su ejecución en acción
agregar_tarea("Estudiar programación imperativa")
agregar_tarea("Pasar el curso de programación")
completar_tarea(1)
completar_tarea(0)
mostrar_tareas()

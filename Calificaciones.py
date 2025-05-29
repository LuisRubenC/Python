def calcular_promedio(lista):
    return sum(lista) / len(lista)

def evaluar_aprobacion(promedio):
    return "Aprobado" if promedio >= 6 else "Reprobado"

estudiantes = []
aprobados = 0
reprobados = 0

cantidad = int(input("¿Cuántos estudiantes deseas registrar? "))

for i in range(cantidad):
    print(f"\nEstudiante {i + 1}:")
    nombre = input("Nombre: ")
    calificaciones = []

    for j in range(3):
        nota = float(input(f"Calificación {j + 1}: "))
        calificaciones.append(nota)

    promedio = calcular_promedio(calificaciones)
    estado = evaluar_aprobacion(promedio)

    if estado == "Aprobado":
        aprobados += 1
    else:
        reprobados += 1

    estudiantes.append({
        "nombre": nombre, 
        "calificaciones": calificaciones,
        "promedio": promedio,
        "estado": estado
    })


print("\n--- Resultados ---")
for est in estudiantes:
    print(f"{est['nombre']}: Promedio = {est['promedio']:.2f}, Estado = {est['estado']}")

print(f"\nTotal Aprobados: {aprobados}")
print(f"Total Reprobados: {reprobados}")

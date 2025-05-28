def calcular_promedio(lista):
    return sum(lista) / len(lista)



estudiantes = []
aprobados = 0
reprobados = 0

cantidad = int(input("¿Cuántos estudiantes deseas registrar? "))

for i in range(cantidad):
    print(f"\n Estudiante {i + 1}:")
    nombre = input("Nombre: ")
    calificaciones = []

    
    })

print("\n --- Resultados --- ")
for est in estudiantes:
    print(f"{est['nombre']}: Promedio = {est['promedio']:.2f}, Estado = {est['estado']}")

print(f"\nTotal Aprobados: {aprobados}")
print(f"Total Reprobados: {reprobados}")

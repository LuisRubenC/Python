
num_estudiantes = int(input("¿Cuántos estudiantes quieres registrar? "))
estudiantes = [None] * num_estudiantes

for i in range(num_estudiantes):
    print(f"\nEstudiante {i + 1}:")
    nombre = input("Nombre del estudiante: ")

    calificaciones = [None] * 4
    calificaciones[0] = nombre  

    for j in range(3):
        nota = float(input(f"Calificación de la materia {j + 1}: "))
        calificaciones[j+1] = nota 

    estudiantes[i] = calificaciones  

print("\nDatos de los estudiantes registrados:")
for i in range(num_estudiantes):
    print(f"Nombre: {estudiantes[i][0]}, Calificaciones: {estudiantes[i][1:]}")

#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

float calcular_promedio(const vector<float>& lista) {
    float suma = 0;
    for (float nota : lista) {
        suma += nota;
    }
    return suma / lista.size();
}

string evaluar_aprobacion(float promedio) {
    return (promedio >= 6.0) ? "Aprobado" : "Reprobado";
}

int main() {
    vector<struct Estudiante> estudiantes;
    int aprobados = 0, reprobados = 0;
    int cantidad;

    cout << "¿Cuantos estudiantes deseas registrar? ";
    cin >> cantidad;
    cin.ignore(); // Limpiar el buffer de entrada

    struct Estudiante {
        string nombre;
        vector<float> calificaciones;
        float promedio;
        string estado;
    };

    for (int i = 0; i < cantidad; ++i) {
        Estudiante est;
        cout << "\nEstudiante " << i + 1 << ":\n";
        cout << "Nombre: ";
        getline(cin, est.nombre);

        for (int j = 0; j < 3; ++j) {
            float nota;
            cout << "Calificacion " << j + 1 << ": ";
            cin >> nota;
            est.calificaciones.push_back(nota);
        }

        cin.ignore();

        est.promedio = calcular_promedio(est.calificaciones);
        est.estado = evaluar_aprobacion(est.promedio);

        if (est.estado == "Aprobado") {
            aprobados++;
        } else {
            reprobados++;
        }

        estudiantes.push_back(est);
    }

    cout << "\n--- Resultados ---\n";
    for (const Estudiante& est : estudiantes) {
        cout << est.nombre << ": Promedio = " << fixed << setprecision(2) << est.promedio 
             << ", Estado = " << est.estado << endl;
    }

    cout << "\nTotal Aprobados: " << aprobados << endl;
    cout << "Total Reprobados: " << reprobados << endl;

    return 0;
}

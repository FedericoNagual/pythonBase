import os
import subprocess
import sys


def ejecutar_semgrep(ruta_analizar):
    # 1. Verificar si la ruta existe
    if not os.path.exists(ruta_analizar):
        print(
            f"Error: La ruta '{ruta_analizar}' no existe.", file=sys.stderr
        )
        return

    print(f"📂 Cambiando al directorio: {ruta_analizar}")
    print("🚀 Ejecutando 'semgrep ci'...")

    try:
        # 2. Ejecutar el comando
        # Usamos 'cwd' (current working directory) para que el comando se ejecute DENTRO de esa carpeta
        resultado = subprocess.run(
            ["semgrep", "ci"],
            cwd=ruta_analizar,
            text=True,  # Captura la salida como texto en vez de bytes
            check=True,  # Lanza una excepción si el comando falla (error de sintaxis, etc.)
        )

        print("\n✅ Análisis de Semgrep completado con éxito.")

    except subprocess.CalledProcessError as e:
        # Semgrep a veces devuelve un código de salida diferente de 0 si encuentra vulnerabilidades (según tu configuración)
        print(
            f"\n⚠️ El proceso terminó. Nota: Si Semgrep encontró hallazgos bloqueantes, es normal que reporte un estado diferente.",
            file=sys.stderr,
        )
    except FileNotFoundError:
        print(
            "\n❌ Error: No se encontró el comando 'semgrep' en el sistema.",
            file=sys.stderr,
        )
        print(
            "Asegúrate de tenerlo instalado y haber ejecutado 'semgrep login' previamente.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    # RUTA DEL PROYECTO: Reemplaza esto con la ruta real en tu computadora
    # Puedes usar rutas absolutas (ej. 'C:/Usuarios/.../juice-shop' o '/home/usuario/.../juice-shop')
    RUTA_PROYECTO = "C:/Users/Lemondata/Desktop/Practica/ProyectoJuiceShop/juice-shop"

    RUTA_PY_GRAFANA = "C:/Users/Lemondata/Documents/ProyectoGIT/WSGrafana/grafana"

    ejecutar_semgrep(RUTA_PY_GRAFANA)
import os
import subprocess
import sys
import shlex


def ejecutar_semgrep(ruta_juice_shop):
    # 1. Verificar si la ruta existe
    if not os.path.exists(ruta_juice_shop):
        print(
            f"Error: La ruta '{ruta_juice_shop}' no existe.", file=sys.stderr
        )
        return

    print(f"📂 Cambiando al directorio: {ruta_juice_shop}")
    print("🚀 Ejecutando 'semgrep scan --config=p/default --text -o resultado.txt'...")

    nombreProyecto = ruta_juice_shop.split("/")[-1].upper()
    nombreArchivoResultado = f"resultado{nombreProyecto}.txt"
    rutaSalida = f"C:/Users/Lemondata/Documents/ProyectosPY/ScriptAutomatizacion/InformesSemgrep/{nombreArchivoResultado}"

    # comandoTexto = f"semgrep scan --config=p/default --text -o {rutaSalida}"
    comandoTexto = f"semgrep scan --config=p/default --text"
    comandoLista = shlex.split(comandoTexto)

    #Seteo para que lea los tipos de caracteres del mundo
    entorno_utf8 = os.environ.copy()
    entorno_utf8["PYTHONIOENCODING"] = "utf-8"
    # entorno_utf8["PYTHONUTF8"] = "1" #variable secreta

    try:
        # 2. Ejecutar el comando
        # Usamos 'cwd' (current working directory) para que el comando se ejecute DENTRO de esa carpeta
        resultado = subprocess.run(
            #semgrep scan --config=p/default --text -o resultado.txt
            comandoLista,
            cwd=ruta_juice_shop,
            capture_output=True, # Captura la salida
            encoding="utf-8",  # Fuerza la lectura en UTF-8
            env=entorno_utf8,  # Le pasa las variables de entorno a Semgrep
            text=True,  # Captura la salida como texto en vez de bytes
            # check=True,  # Lanza una excepción si el comando falla (error de sintaxis, etc.)
            check=False,  # Probando para escribir el archivo desde py
        )

        with open(rutaSalida, "w", encoding="utf-8") as archivo_salida:
            archivo_salida.write(resultado.stdout)
            # Si Semgrep escupió algún error interno, lo guardamos también para que lo puedas ver
            if resultado.stderr:
                archivo_salida.write("\n--- LOGS DE ERRORES DE SEMGREP ---\n")
                archivo_salida.write(resultado.stderr)
                archivo_salida.write("\n----------------------------------\n")

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
    # RUTA_PROYECTO_JUICE = "C:/Users/Lemondata/Desktop/Practica/ProyectoJuiceShop/juice-shop"
    #
    # RUTA_PY_GRAFANA = "C:/Users/Lemondata/Documents/ProyectoGIT/WSGrafana/grafana"
    if (sys.argv) > 1:
        ruta = sys.argv[1]
        ejecutar_semgrep(RUTA_PY_GRAFANA)
    else:
        print("\n❌ Error: No se encontraron parametros de ruta del proyecto a analizar")
        print("Uso correcto: python analizarPdfParametro.py <ruta>")
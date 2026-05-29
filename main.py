#!/home/p4/RPI_workspace/.workspace/bin/python
# test_servos.py
import time
from functions.myservos import ControladorServo

# Instanciamos un servo conectado al GPIO 12
servo_brazo = ControladorServo(pin_gpio=12, angulo_min=0, angulo_max=180)

print("\n--- 🤖 Control Manual de Servo ---")
print("Escribe un ángulo entre 0 y 180.")
print("Escribe 'q' para salir del programa.")
print("----------------------------------\n")

try:
    while True:
        # 1. Pedir el input al usuario en la terminal
        entrada = input("👉 Ingresa el ángulo deseado: ")
        
        # 2. Comprobar si el usuario quiere salir
        if entrada.lower() == 'q':
            print("Saliendo del control manual...")
            break # Rompe el bucle y va directo al "finally"
            
        # 3. Intentar convertir el texto a número y mover el servo
        try:
            angulo_usuario = float(entrada)
            
            # Tu clase ControladorServo ya protege los límites mecánicos, 
            # pero es bueno darle feedback al usuario en la pantalla:
            if 0 <= angulo_usuario <= 180:
                servo_brazo.mover_a(angulo_usuario)
            else:
                print("⚠️ Aviso: El ángulo ideal debe estar entre 0 y 180.")
                servo_brazo.mover_a(angulo_usuario) # Lo enviamos igual, tu clase lo limitará
                
        except ValueError:
            # Si el usuario escribe letras como "hola", evitamos que el programa explote
            print("❌ Error: Entrada inválida. Por favor ingresa solo números.")

except KeyboardInterrupt:
    # Esto captura si presionas Ctrl+C en la terminal para forzar la salida
    print("\nPrograma interrumpido por el usuario (Ctrl+C).")

finally:
    # IMPORTANTE: Desactivar el pulso al terminar el script
    servo_brazo.apagar()
    print("💤 Secuencia finalizada y servo apagado de forma segura.")
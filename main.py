#!/home/p4/RPI_workspace/.workspace/bin/python
# test_servos.py
import time
from functions.myservos import ControladorServo

# Instanciamos un servo SG90 estándar conectado al GPIO 18
servo_brazo = ControladorServo(pin_gpio=12, angulo_min=0, angulo_max=180)

try:
    print("Iniciando secuencia de prueba...")
    
    # Mover a posiciones fijas
    servo_brazo.mover_a(0)
    time.sleep(1)
    
    servo_brazo.mover_a(90)
    time.sleep(1)
    
    servo_brazo.mover_a(180)
    time.sleep(1)
    
    # Movimiento fluido tipo barrido (Suave)
    print("Haciendo un barrido de ida y vuelta...")
    for angulo in range(180, -1, -5):
        servo_brazo.mover_a(angulo)
        time.sleep(0.05)

finally:
    # IMPORTANTE: Desactivar el pulso al terminar el script
    servo_brazo.apagar()